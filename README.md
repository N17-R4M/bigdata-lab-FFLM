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
Dataset: Microdados do ENEM 2024     
Formato Original: Arquivos .csv     

#### Problema:
O ENEM atua como o principal mecanismo de acesso ao ensino superior no Brasil, mas os seus resultados refletem as profundas desigualdades do país. O problema reside na dificuldade de mapear como variáveis socieconômicas, como renda familiar, histórico escolar e acesso a bens, se combinam para criar barreiras ao desempenho dos candidatos. Embora o INEP forneça um grande volume de dados, essas informações aparecem de forma dispersa, tornando complexa a tarefa de identificar perfis específicos de alunos que compartilham as mesmas limitação sociais e econômicas.
O projeto resolve essa questão ao aplicar o algoritmo K-Means para transformar dados multimensionais em grupos claros e interpretáveis. A classificação proposta permite superar a análise simplista de variáveis isoladas, criando perfis consolidados que revelam a real desigualdade entre os participantes

#### Processo de Coleta:
A solução proposta utiliza as bibliotecas requests para os dowload automatizado e zipfile para a manipulação dos arquivos, garantindo que o processo seja replicável sem intervenção manual. Dado o tamanho dos arquivos de 2024, a estratégia de leitura utiliza o processamento em blocos através da biblioteca pandas, que evita o estoura da memória RAM ao carregar apenas as colunas necessárias para o modelo de K-means.

#### Critério de seleção de dados:
Os dados foram selecionados diretamente do site do INEP, fonte oficial dos dados abertos do ENEM.

#### Roadmap do projeto:
- [x] Planejamento
- [x] Pré-processamento e ingestão
- [ ] Análise Exploratória e Limpeza
- [ ] Aplicação de ML
