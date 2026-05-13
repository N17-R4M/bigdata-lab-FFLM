| NOME DA VARIÁVEL | Descrição | Tamanho | Tipo | Categorias (Valores) |
| :--- | :--- | :---: | :---: | :--- |
| **NU_INSCRICAO** | Número de inscrição | 12 | Numérica | *Variável Numérica Única* |
| **NU_ANO** | Ano do Enem | 4 | Numérica | *Ano de referência (Ex: 2024)* |
| **TP_FAIXA_ETARIA** | Faixa etária | 2 | Numérica | 1 = Menor de 17 anos<br>2 = 17 anos<br>3 = 18 anos<br>4 = 19 anos<br>5 = 20 anos<br>6 = 21 anos<br>7 = 22 anos<br>8 = 23 anos<br>9 = 24 anos<br>10 = 25 anos<br>11 = Entre 26 e 30 anos<br>12 = Entre 31 e 35 anos<br>13 = Entre 36 e 40 anos<br>14 = Entre 41 e 45 anos<br>15 = Entre 46 e 50 anos<br>16 = Entre 51 e 55 anos<br>17 = Entre 56 e 60 anos<br>18 = Entre 61 e 65 anos<br>19 = Entre 66 e 70 anos<br>20 = Maior de 70 anos |
| **TP_SEXO** | Sexo | 1 | Alfanumérica | M = Masculino<br>F = Feminino |
| **TP_ESTADO_CIVIL** | Estado Civil | 1 | Numérica | 0 = Não informado<br>1 = Solteiro(a)<br>2 = Casado(a)/Mora com companheiro(a)<br>3 = Divorciado(a)/Desquitado(a)/Separado(a)<br>4 = Viúvo(a) |
| **TP_COR_RACA** | Cor/raça | 1 | Numérica | 0 = Não declarado<br>1 = Branca<br>2 = Preta<br>3 = Parda<br>4 = Amarela<br>5 = Indígena<br>6 = Não dispõe da informação |
| **TP_NACIONALIDADE** | Nacionalidade | 1 | Numérica | 0 = Não informado<br>1 = Brasileiro(a)<br>2 = Brasileiro(a) Naturalizado(a)<br>3 = Estrangeiro(a)<br>4 = Brasileiro(a) Nato(a), nascido(a) no exterior |
| **TP_ST_CONCLUSAO** | Situação de conclusão do Ensino Médio | 1 | Numérica | 1 = Já concluí o Ensino Médio<br>2 = Estou cursando e concluirei o EM em 2024<br>3 = Estou cursando e concluirei o EM após 2024<br>4 = Não concluí e não estou cursando o EM |
| **TP_ANO_CONCLUIU** | Ano de Conclusão do Ensino Médio | 2 | Numérica | 0 = Não informado<br>1 = 2023<br>2 = 2022<br>3 = 2021<br>4 = 2020<br>5 = 2019<br>6 = 2018<br>7 = 2017<br>8 = 2016<br>9 = 2015<br>10 = 2014<br>11 = 2013<br>12 = 2012<br>13 = 2011<br>14 = 2010<br>15 = 2009<br>16 = 2008<br>17 = 2007<br>18 = Antes de 2007 |
| **TP_ENSINO** | Tipo de instituição de conclusão do EM | 1 | Numérica | 1 = Ensino Regular<br>2 = Educação Especial |
| **IN_TREINEIRO** | Indica se é treineiro | 1 | Numérica | 1 = Sim<br>0 = Não |
| **CO_MUNICIPIO_PROVA**| Código do município da prova | 7 | Numérica | *Código IBGE (Região/UF/Município)* |
| **NO_MUNICIPIO_PROVA**| Nome do município da prova | 150 | Alfanumérica | *Nome da cidade* |
| **CO_UF_PROVA** | Código da UF da prova | 2 | Alfanumérica | *Código numérico da UF* |
| **SG_UF_PROVA** | Sigla da UF da prova | 2 | Alfanumérica | *Sigla (Ex: SP, RJ)* |
| **Q001** | Escolaridade do pai/homem responsável | 1 | Alfanumérica | A = Nunca estudou<br>B = Não completou 4ª série/5º ano<br>C = Completou 5º ano, mas não 9º ano<br>D = Completou 9º ano, mas não EM<br>E = Completou EM, mas não Faculdade<br>F = Completou Faculdade, mas não Pós<br>G = Completou Pós-graduação<br>H = Não sei |
| **Q002** | Escolaridade da mãe/mulher responsável | 1 | Alfanumérica | A = Nunca estudou<br>B = Não completou 4ª série/5º ano<br>C = Completou 5º ano, mas não 9º ano<br>D = Completou 9º ano, mas não EM<br>E = Completou EM, mas não Faculdade<br>F = Completou Faculdade, mas não Pós<br>G = Completou Pós-graduação<br>H = Não sei |
| **Q003** | Grupo de ocupação do pai | 1 | Alfanumérica | A = Grupo 1 (Lavrador, etc.)<br>B = Grupo 2 (Diarista, vendedor, etc.)<br>C = Grupo 3 (Padeiro, mecânico, etc.)<br>D = Grupo 4 (Professor, técnico, etc.)<br>E = Grupo 5 (Médico, engenheiro, etc.)<br>F = Não sei |
| **Q004** | Grupo de ocupação da mãe | 2 | Numérica | A = Grupo 1 (Lavradora, etc.)<br>B = Grupo 2 (Diarista, vendedora, etc.)<br>C = Grupo 3 (Padeira, mecânica, etc.)<br>D = Grupo 4 (Professora, técnica, etc.)<br>E = Grupo 5 (Médica, engenheira, etc.)<br>F = Não sei |
| **Q005** | Quantas pessoas moram na residência? | 2 | Numérica | 1 a 20 (Número de moradores) |
| **Q006** | Você possui renda? | 1 | Alfanumérica | A = Não<br>B = Sim |
| **Q007** | Renda mensal da família | 1 | Alfanumérica | A = Nenhuma Renda<br>B = Até R$ 1.412,00<br>C = De R$ 1.412,01 até R$ 2.118,00<br>D = De R$ 2.118,01 até R$ 2.824,00<br>E = De R$ 2.824,01 até R$ 3.530,00<br>F = De R$ 3.530,01 até R$ 4.236,00<br>G = De R$ 4.236,01 até R$ 5.648,00<br>H = De R$ 5.648,01 até R$ 7.060,00<br>I = De R$ 7.060,01 até R$ 8.472,00<br>J = De R$ 8.472,01 até R$ 9.884,00<br>K = De R$ 9.884,01 até R$ 11.296,00<br>L = De R$ 11.296,01 até R$ 12.708,00<br>M = De R$ 12.708,01 até R$ 14.120,00<br>N = De R$ 14.120,01 até R$ 16.944,00<br>O = De R$ 16.944,01 até R$ 21.180,00<br>P = De R$ 21.180,01 até R$ 28.240,00<br>Q = Acima de R$ 28.240,00 |
| **Q008** | Contrata empregado(a) doméstico(a)? | 1 | Alfanumérica | A = Não<br>B = Sim, 1 ou 2 dias/semana<br>C = Sim, 3 ou 4 dias/semana<br>D = Sim, 5 ou mais dias/semana |
| **Q009** | Existe banheiro em casa? | 1 | Alfanumérica | A = Não<br>B = Sim, um<br>C = Sim, dois<br>D = Sim, três ou mais |
| **Q010** | Existe quarto para dormir? | 1 | Alfanumérica | A = Não<br>B = Sim, um<br>C = Sim, dois<br>D = Sim, três ou mais |
| **Q011** | Possui carro? | 1 | Alfanumérica | A = Não<br>B = Sim, um<br>C = Sim, dois<br>D = Sim, três ou mais |
| **Q012** | Possui motocicleta? | 1 | Alfanumérica | A = Não<br>B = Sim, uma<br>C = Sim, duas<br>D = Sim, três ou mais |
| **Q013** | Existe geladeira? | 1 | Alfanumérica | A = Não<br>B = Sim, uma<br>C = Sim, duas<br>D = Sim, três ou mais |
| **Q014** | Existe freezer independente? | 1 | Alfanumérica | A = Não<br>B = Sim |
| **Q015** | Existe máquina de lavar roupa? | 1 | Alfanumérica | A = Não<br>B = Sim |
| **Q016** | Existe micro-ondas? | 1 | Alfanumérica | A = Não<br>B = Sim |
| **Q017** | Existe aspirador de pó? | 1 | Alfanumérica | A = Não<br>B = Sim |
| **Q018** | Existe aparelho de TV? | 1 | Alfanumérica | A = Não<br>B = Sim, uma<br>C = Sim, duas<br>D = Sim, três ou mais |
| **Q019** | Existe TV por assinatura? | 1 | Alfanumérica | A = Não<br>B = Sim |
| **Q020** | Existe rede wi-fi? | 1 | Alfanumérica | A = Não<br>B = Sim |
| **Q021** | Existe computador/notebook? | 1 | Alfanumérica | A = Não<br>B = Sim, um<br>C = Sim, dois<br>D = Sim, três<br>E = Sim, quatro ou mais |
| **Q022** | Possui telefone celular? | 1 | Alfanumérica | A = Não<br>B = Sim, um<br>C = Sim, dois<br>D = Sim, três ou mais<br>E = Sim, quatro ou mais |
| **Q023** | Tipo de escola no Ensino Médio | 1 | Alfanumérica | A = Somente pública<br>B = Parte pública/privada (sem bolsa)<br>C = Parte pública/privada (com bolsa integral)<br>D = Somente privada (sem bolsa)<br>E = Somente privada (com bolsa integral)<br>F = Não frequentei escola de EM |
