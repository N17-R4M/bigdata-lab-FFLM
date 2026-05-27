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

#### Relato Machine Learning (Clusterização com K-means e K-medoids):

Foi desenvolvido um pipeline analítico para investigar o impacto do contexto socioeconômico no desempenho dos estudantes, utilizando aprendizado não supervisionado para agrupar os municípios brasileiros. A construção desses perfis estruturais baseou-se em indicadores que traduzem a realidade local, abrangendo características como os níveis de exclusão digital, a proporção de alunos dependentes da rede pública, a taxa de abstenção nas provas e a média geral das notas.

Para garantir a confiabilidade dos resultados e atestar a capacidade de generalização do modelo, a base de dados foi separada antes de iniciar a etapa de clusterização. O processo destinou 75% dos dados para o treinamento dos algoritmos e isolou os 25% restantes exclusivamente para a validação.

A modelagem foi estruturada na aplicação e comparação de dois algoritmos: K-Means e K-Medoids. O trabalho iniciou com o K-Means, que, após a padronização dos dados e diversos testes iterativos, apontou que a divisão ideal da base seria em quatro clusters. Em seguida, o K-Medoids foi implementado como uma alternativa metodológica, utilizando instâncias reais da base para ancorar o centro de cada grupo. Essa escolha teve como objetivo testar se o modelo apresentaria uma maior resistência e precisão ao lidar com cidades de indicadores outliers.

O desempenho da clusterização foi avaliado por métricas focadas na consistência e no isolamento dos grupos formados. Utilizou-se o Silhouette Score para medir se cada município estava bem alocado em seu respectivo cluster, complementado pelo Elbow, que checou o nível de dispersão interna e o distanciamento entre os agrupamentos. O estudo foi concluído com a geração de uma matriz comparativa utilizando os dados de teste.

#### Roadmap do projeto:
- [x] Planejamento
- [x] Pré-processamento e ingestão
- [ ] Análise Exploratória e Limpeza
- [ ] Aplicação de ML
