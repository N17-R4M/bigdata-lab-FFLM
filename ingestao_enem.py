import os
import requests
import zipfile
import polars as pl
from pathlib import Path
from io import BytesIO

# Caminho para o INEP
URL_ENEM = "https://download.inep.gov.br/microdados/microdados_enem_2024.zip"
DOWNLOADS_FEDORA = Path.home() / "Downloads"
DIR_PROJETOS = Path.cwd()
DIR_RAW = DIR_PROJETOS / "data" / "raw"
DIR_PROCESSED = DIR_PROJETOS / "data" / "processed"

# Arquivos para extrair e processar
ARQUIVOS_ALVO = ["PARTICIPANTES_2024.csv", "RESULTADOS_2024.csv"]

def inicializar_ambiente():
    DIR_RAW.mkdir(parents=True, exist_ok=True)
    DIR_PROCESSED.mkdir(parents=True, exist_ok=True)

def obter_fonte_zip():
    # Verifica se o ZIP já está nos Downloads, se não baixa da web
    zips_downloads = list(DOWNLOADS_FEDORA.glob("microdados_enem_2024.zip"))
    if zips_downloads:
        print(f"Arquivo ZIP encontrado na pasta Downloads: {zips_downloads[0]}")
        return zips_downloads[0]
    
    headers = {'User-Agent': 'Mozilla/5.0'}
    print("Baixando microdados do portal do INEP")
    try:
        response = requests.get(URL_ENEM, headers=headers, stream=True, verify=False)
        response.raise_for_status()
        return BytesIO(response.content)
    except Exception as e:
        print(f"Erro no download: {e}")
        return None

def processar_arquivo(csv_path):
    # Lógica de conversão iconv e salvamento em Parquet
    try:
        csv_utf8 = csv_path.with_name(csv_path.stem + "_utf8.csv")
        parquet_final = DIR_PROCESSED / (csv_path.stem.lower() + ".parquet")

        # Conversão para UTF-8
        if not csv_utf8.exists():
            print(f"Convertendo {csv_path.name} para UTF-8...")
            os.system(f"iconv -f latin1 -t utf8 '{csv_path}' -o '{csv_utf8}'")
        
        # Conversão para Parquet via Polars
        print(f"Gerando Parquet: {parquet_final.name}")
        lf = pl.scan_csv(
            csv_utf8,
            separator=';',
            encoding='utf8',
            infer_schema_length=20000,
            ignore_errors=True
        )
        lf.sink_parquet(parquet_final, compression="zstd")
        print(f"Sucesso: {parquet_final.name}")
        
    except Exception as e:
        print(f"Erro ao processar {csv_path.name}: {e}")

def extrair_alvos(fonte_zip):
    try:
        with zipfile.ZipFile(fonte_zip) as z:
            arquivos_no_zip = z.namelist()
            
            for alvo in ARQUIVOS_ALVO:
                # Busca o caminho real dentro do ZIP 
                match = [f for f in arquivos_no_zip if alvo in f]
                if match:
                    target = match[0]
                    print(f"Extraindo: {target}")
                    z.extract(target, DIR_RAW)
                    
                    # Processa o arquivo extraído
                    caminho_extraido = DIR_RAW / target
                    processar_arquivo(caminho_extraido)
                else:
                    print(f"Aviso: Arquivo {alvo} não encontrado no ZIP.")
                    
    except Exception as e:
        print(f"Erro na extração: {e}")

if __name__ == "__main__":
    inicializar_ambiente()
    zip_fonte = obter_fonte_zip()
    
    if zip_fonte:
        extrair_alvos(zip_fonte)
        print("\nProcessamento de todos os arquivos concluído.")
    else:
        print("Não foi possível localizar a fonte de dados.")