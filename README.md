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

Link Mongo DB:
mongodb+srv://lucaspoliveira1907:ProjetoMBA123@projetomba.pweru3q.mongodb.net/?appName=ProjetoMBA
Senha: ProjetoMBA123

#### Roadmap do projeto:
- [x] Planejamento
- [x] Pré-processamento e ingestão
- [ ] Análise Exploratória e Limpeza
- [ ] Aplicação de ML
