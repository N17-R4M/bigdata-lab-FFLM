# bigdata-lab-FFLM

#### Projeto:
Projeto hands-on em bigdata e analytics do curso de MBA em Engenharia de Dados da Universidade Presbiteriana Mackenzie.

#### Integrantes:
- Felipe Araujo - RA 10732144 - Nickname: Feddcat04
- Felipe Lage - RA 10731861 - Nickname: FelipeLage91
- Lucas Oliveira - RA 10732279 - Nickname: lucaspoliveira1907-droid
- Martin Heib - RA 10734895 - Nickname: N17-R4M

#### Sobre os dados:
O grupo utilizou dados abertos do Instituto Nacional de Estudos e Pesquisas Educacionais (INEP) através do portal de dados abertos do governo federal.     
[Link](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem)     
Datasets: participantes.csv, resultados.csv      
Formato Original: Arquivos .csv     

#### Problema:
O ENEM atua como o principal mecanismo de acesso ao ensino superior no Brasil, mas os seus resultados refletem as profundas desigualdades do país. O problema reside na dificuldade de mapear como variáveis socieconômicas, como renda familiar, histórico escolar e acesso a bens, e compreender como se combinam para criar barreiras ao desempenho dos candidatos. 

Embora o INEP forneça um grande volume de dados, essas informações aparecem de forma dispersa, tornando complexa a tarefa de identificar perfis específicos de alunos que compartilham as mesmas limitações sociais e econômicas, e identificar os impactos dessas variáveis em seu desempenho.

#### Processo de Coleta:
Começamos criando um clone do git no PC para manter os documentos do projeto juntos e instalando ferramentas de desenvolvimento no ambiente Linux
Porém para isso (Linux Fedora), foi necessário criar um ambiente virtual na pasta para não causar conflitos com pip, já que precisaríamos que a biblioteca Polars pudesse ser importada corretamente.

O processo detalhado de input de dados está descrito no documento `Ingestão dos Dados.md` na pasta docs.

#### Critério de seleção de dados:
Os dados foram selecionados diretamente do site do INEP, fonte oficial dos dados abertos do ENEM. Os datasets foram escolhidos porque queríamos bases com dataset alto volume de varíaveis para para que pudéssemos aplicar técnicas de exploração e limpeza.

#### Relato Machine Learning (Clusterização com K-means e K-medoids):

Foi desenvolvido um pipeline analítico para investigar o impacto do contexto socioeconômico no desempenho dos estudantes, utilizando aprendizado não supervisionado para agrupar os municípios brasileiros. A construção desses perfis estruturais baseou-se em indicadores que traduzem a realidade local, abrangendo características como os níveis de exclusão digital, a proporção de alunos dependentes da rede pública, a taxa de abstenção nas provas e a média geral das notas.

Para garantir a confiabilidade dos resultados e atestar a capacidade de generalização do modelo, a base de dados foi separada antes de iniciar a etapa de clusterização. O processo destinou 75% dos dados para o treinamento dos algoritmos e isolou os 25% restantes exclusivamente para a validação.

A modelagem foi estruturada na aplicação e comparação de dois algoritmos: K-Means e K-Medoids. O trabalho iniciou com o K-Means, que, após a padronização dos dados e diversos testes iterativos, apontou que a divisão ideal da base seria em quatro clusters. Em seguida, o K-Medoids foi implementado como uma alternativa metodológica, utilizando instâncias reais da base para ancorar o centro de cada grupo. Essa escolha teve como objetivo testar se o modelo apresentaria uma maior resistência e precisão ao lidar com cidades de indicadores outliers.

O desempenho da clusterização foi avaliado por métricas focadas na consistência e no isolamento dos grupos formados. Utilizou-se o Silhouette Score para medir se cada município estava bem alocado em seu respectivo cluster, complementado pelo Elbow, que checou o nível de dispersão interna e o distanciamento entre os agrupamentos. O estudo foi concluído com a geração de uma matriz comparativa utilizando os dados de teste.

# Pipeline geral

Este projeto implementa uma esteira completa de dados (ETL) baseada na Arquitetura Medalhão utilizando o ecossistema local com Docker, MongoDB, Polars, Pandas e VS Code. 

O objetivo é extrair de forma resiliente os mais de 4,3 milhões de registros dos Microdados do ENEM 2024, processá-los de forma otimizada para restrição de memória RAM e aplicar algoritmos de aprendizado não-supervisionado (Clustering) para análise municipal.

## Arquitetura e Fluxo do Pipeline     
O ciclo de vida dos dados está dividido estritamente em três etapas através de notebooks modulares:

### Camada Bronze (ingestao_bronze.ipynb):      
Download multithread automatizado do portal de dados abertos do INEP, extração seletiva dos arquivos, conversão de encodamento (latin1 para utf-8 via iconv) e ingestão em lotes (batching) para o repositório NoSQL bruto.

### Camada Silver (Analise_Exploratória.ipynb): 
Leitura otimizada de coleções no MongoDB aplicando projeções estruturadas e técnicas de redução de consumo de memória (downcasting).      
Realiza o tratamento de valores nulos, engenharia de atributos socioeconômicos e agrega os dados a nível municipal. O resultado limpo é persistido em um banco isolado.

### Camada Gold / ML (ML_.ipynb):       
Ingestão direta dos dados municipais consolidados e execução da esteira de Machine Learning. Realiza split estatístico de validação, normalização de escala e compara o agrupamento geo-educacional utilizando os algoritmos K-Means e K-Medoids.

Estrutura do RepositórioPlaintextprojeto_enem/     
├── .venv/                  # Ambiente virtual Python (Ignorado no Git)     
├── data/                   # Diretório de armazenamento de dados (Ignorado no Git)     
│   └── raw/                # CSVs brutos extraídos do INEP     
├── .gitignore              # Regras de exclusão de arquivos para o Git     
├── docker-compose.yml      # Configuração de Infraestrutura como Código (IaC) do Banco NoSQL     
├── ingestao_bronze.ipynb   # Notebook de Ingestão e Carga Raw     
├── Analise_Exploratória.ipynb # Notebook de EDA, Limpeza e Carga Silver     
└── ML_.ipynb               # Notebook de Modelagem e Clustering (Machine Learning)     

## Pré-requisitos do Sistema     

Antes de iniciar, certifique-se de possuir instalado:  
- VS Code (com as extensões oficiais Python e Jupyter instaladas)
- Docker e Docker Compose

- Usuários Linux: Docker Engine e plugin do Compose nativos.

- Usuários Windows: Docker Desktop configurado obrigatoriamente com o backend do WSL2 (Windows Subsystem for Linux) para permitir a execução nativa de comandos de terminal como o iconv.

## Passo a Passo para Instalação e Execução

1. Clonar o Repositório
2. Configurar o Ambiente Virtual Python (.venv)     
- Para garantir o isolamento das dependências de dados sem interferir nos pacotes globais do sistema, configure o ambiente virtual:
- No Linux:     
`Bashpython3 -m venv .venv
source .venv/bin/activate`

- No Windows (PowerShell):     
`PowerShellpython -m venv .venv
.\.venv\Scripts\Activate.ps1`

- Com o ambiente ativado (.venv), atualize o gerenciador de pacotes e instale as dependências:     
`Bashpip install --upgrade pip`     
`pip install pymongo polars requests pandas numpy matplotlib seaborn scikit-learn scikit-learn-extra`

3. Subir a Infraestrutura do Banco de Dados (Docker)
- O repositório contém a definição de Infraestrutura como Código (docker-compose.yml). Para provisionar a instância local do MongoDB pré-configurada com credenciais administrativas e persistência em volume separado, execute:
`Bashdocker compose up -d`

4. Execução do Pipeline no VS Code     
- Abra a pasta do projeto no VS Code:
- Abra o arquivo ingestao_bronze.ipynb.
- No canto superior direito do VS Code, clique em Select Kernel $\rightarrow$ Python Environments e aponte estritamente para o interpretador contido dentro da pasta ./.venv/bin/python.

- Siga a ordem sequencial estrita de execução dos arquivos:
- Passo 1: ingestao_bronze.ipynb     
  O que faz: Realiza o download do arquivo compactado do INEP e extrai os arquivos PARTICIPANTES_2024.csv e RESULTADOS_2024.csv. Em seguida, utiliza o utilitário nativo de sistema iconv para recodificar os arquivos para UTF-8 e faz a carga em lotes de 50.000 linhas na base enem_bronze do seu Docker.     
  Validação: Ao finalizar, o log exibirá o progresso completo até a marca de 4.332.944 de registros inseridos com sucesso.
- Passo 2: Analise_Exploratória.ipynb     
  O que faz: Conecta à camada bruta. Aplica projeções em nível de banco de dados para buscar apenas as colunas selecionadas no escopo do projeto, evitando o estouro de memória RAM.
  Otimização de Engenharia: Transforma colunas de strings redundantes em tipos category e reduz o peso das notas numéricas de float64 para float32. Consolida e agrupa os dados socioeconômicos e de desempenho por município e salva a base tratada no banco de dados isolado enem_silver.
- Passo 3: ML_.ipynb     
  O que faz: Puxa a base consolidada de municípios da camada Silver (uma carga leve de aproximadamente 5.500 linhas). Executa a análise de hiperparâmetros para encontrar o número ideal de agrupamentos ($K=4$) e treina os modelos K-Means e K-Medoids, comparando a eficácia matemática por meio das métricas de Silhouette Score e Davies-Bouldin.

  ## Detalhes de Credenciais e Segurança     
  As credenciais configuradas na infraestrutura do container e pré-mapeadas nas strings de conexões internas dos scripts são:
  - Banco de Dados: MongoDB (Porta padrão 27017)
  - Usuário Admin: admin
  - Senha Admin: ProjetoMBA123
  - String de Conexão Local: mongodb://admin:ProjetoMBA123@localhost:27017/?authSource=admin
