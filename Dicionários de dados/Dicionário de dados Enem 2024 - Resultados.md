 DICIONÁRIO DE VARIÁVEIS - RESULTADOS ENEM 2024

Este documento descreve as variáveis contidas no microdados do ENEM 2024.

## 1. DADOS DO PARTICIPANTE

| Nome da Variável | Descrição | Tamanho | Tipo |
| :--- | :--- | :--- | :--- |
| NU_SEQUENCIAL | Número sequencial da linha de resultados¹ | 12 | Numérica |
| NU_ANO | Ano do Enem | 4 | Numérica |

## 2. DADOS DA ESCOLA

| Nome da Variável | Descrição | Tamanho | Tipo | Categoria / Descrição |
| :--- | :--- | :--- | :--- | :--- |
| CO_ESCOLA | Código da Escola de conclusão do ensino médio² | 8 | Numérica | - |
| CO_MUNICIPIO_ESC | Código do município da escola | 7 | Numérica | 1º dígito: Região<br>1º e 2º dígitos: UF<br>3º ao 6º: Município<br>7º: Dígito verificador |
| NO_MUNICIPIO_ESC | Nome do município da escola | 150 | Alfanumérica | - |
| CO_UF_ESC | Código da Unidade da Federação da escola | 2 | Numérica | - |
| SG_UF_ESC | Sigla da Unidade da Federação da escola | 2 | Alfanumérica | - |
| TP_DEPENDENCIA_ADM_ESC | Dependência administrativa | 1 | Numérica | 1: Federal<br>2: Estadual<br>3: Municipal<br>4: Privada |
| TP_LOCALIZACAO_ESC | Localização | 1 | Numérica | 1: Urbana<br>2: Rural |
| TP_SIT_FUNC_ESC | Situação de funcionamento | 1 | Numérica | 1: Em atividade<br>2: Paralisada<br>3: Extinta<br>4: Extinta em anos anteriores |

## 3. DADOS DO LOCAL DE APLICAÇÃO DA PROVA

| Nome da Variável | Descrição | Tamanho | Tipo | Categoria / Descrição |
| :--- | :--- | :--- | :--- | :--- |
| CO_MUNICIPIO_PROVA | Código do município da aplicação | 7 | Numérica | Mesma lógica de CO_MUNICIPIO_ESC |
| NO_MUNICIPIO_PROVA | Nome do município da aplicação | 150 | Alfanumérica | - |
| CO_UF_PROVA | Código da UF da aplicação | 2 | Alfanumérica | - |
| SG_UF_PROVA | Sigla da UF da aplicação | 2 | Alfanumérica | - |

## 4. DADOS DA PROVA OBJETIVA

| Nome da Variável | Descrição | Tamanho | Tipo | Categoria / Valores |
| :--- | :--- | :--- | :--- | :--- |
| TP_PRESENCA_CN | Presença em Ciências da Natureza | 1 | Numérica | 0: Faltou<br>1: Presente<br>2: Eliminado |
| TP_PRESENCA_CH | Presença em Ciências Humanas | 1 | Numérica | 0: Faltou<br>1: Presente<br>2: Eliminado |
| TP_PRESENCA_LC | Presença em Linguagens e Códigos | 1 | Numérica | 0: Faltou<br>1: Presente<br>2: Eliminado |
| TP_PRESENCA_MT | Presença em Matemática | 1 | Numérica | 0: Faltou<br>1: Presente<br>2: Eliminado |
| CO_PROVA_CN | Código do tipo de prova (CN) | 4 | Numérica | Ex: 1419: Azul, 1420: Amarela, 1421: Verde, 1422: Cinza... |
| CO_PROVA_CH | Código do tipo de prova (CH) | 4 | Numérica | Ex: 1383: Azul, 1384: Amarela, 1385: Branca, 1386: Verde... |
| CO_PROVA_LC | Código do tipo de prova (LC) | 4 | Numérica | Ex: 1395: Azul, 1396: Amarela, 1397: Verde, 1398: Branca... |
| CO_PROVA_MT | Código do tipo de prova (MT) | 4 | Numérica | Ex: 1407: Azul, 1408: Amarela, 1409: Verde, 1410: Cinza... |
| NU_NOTA_CN | Nota de Ciências da Natureza | 9 | Numérica | - |
| NU_NOTA_CH | Nota de Ciências Humanas | 9 | Numérica | - |
| NU_NOTA_LC | Nota de Linguagens e Códigos | 9 | Numérica | - |
| NU_NOTA_MT | Nota de Matemática | 9 | Numérica | - |
| TX_RESPOSTAS_CN | Vetor de respostas (CN) | 45 | Alfanumérica | A,B,C,D,E, * (dupla), . (branco) |
| TX_RESPOSTAS_CH | Vetor de respostas (CH) | 45 | Alfanumérica | A,B,C,D,E, * (dupla), . (branco) |
| TX_RESPOSTAS_LC | Vetor de respostas (LC) | 45 | Alfanumérica | A,B,C,D,E, * (dupla), . (branco), 9 (não apres.) |
| TX_RESPOSTAS_MT | Vetor de respostas (MT) | 45 | Alfanumérica | A,B,C,D,E, * (dupla), . (branco) |
| TP_LINGUA | Língua Estrangeira | 1 | Numérica | 0: Inglês<br>1: Espanhol |
| TX_GABARITO_CN | Gabarito oficial (CN) | 45 | Alfanumérica | - |
| TX_GABARITO_CH | Gabarito oficial (CH) | 45 | Alfanumérica | - |
| TX_GABARITO_LC | Gabarito oficial (LC) | 50 | Alfanumérica | - |
| TX_GABARITO_MT | Gabarito oficial (MT) | 45 | Alfanumérica | - |

## 5. DADOS DA REDAÇÃO

| Nome da Variável | Descrição | Tamanho | Tipo | Categoria / Valores |
| :--- | :--- | :--- | :--- | :--- |
| TP_STATUS_REDACAO | Situação da redação | 1 | Numérica | 1: Sem problemas<br>2: Anulada<br>3: Cópia Texto Motivador<br>4: Em Branco<br>6: Fuga ao tema<br>7: Não atend. tipo textual<br>8: Texto insuficiente<br>9: Parte desconectada |
| NU_NOTA_COMP1 | Nota Competência 1 | 9 | Numérica | Domínio escrita formal |
| NU_NOTA_COMP2 | Nota Competência 2 | 9 | Numérica | Compreensão do tema |
| NU_NOTA_COMP3 | Nota Competência 3 | 9 | Numérica | Seleção/Organização de info |
| NU_NOTA_COMP4 | Nota Competência 4 | 9 | Numérica | Mecanismos linguísticos |
| NU_NOTA_COMP5 | Nota Competência 5 | 9 | Numérica | Proposta de intervenção |
| NU_NOTA_REDACAO | Nota final da redação | 9 | Numérica | - |
