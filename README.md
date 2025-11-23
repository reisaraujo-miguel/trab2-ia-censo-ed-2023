# Trabalho de IA 2025: machine learning e mineração de dados

## Alunos:
- Miguel Reis de Araújo (Líder), NºUSP: 12752457
- Jean Patrick Ngandu Mamani (Vice-líder), NºUSP: 14712678
- Camila Aya Saito, NºUSP: 15635649
- Vinicius Moraes de Carvalho, NºUSP: 15642432
- Victoria Fávero Nunes, NºUSP: 15698302

## Tema:

O problema consiste em utilizar os dados do Censo Escolar para fazer uma análise sobre a infraestrutura das escolas, em que elas seriam agrupadas tendo como base atributos que impactam a infraestrutura. Essa análise é importante, pois a infraestrutura de uma escola tem forte influência na capacidade de aprendizado de um aluno. Portanto, para se descobrir se uma escola é boa ou não, é fundamental saber analisar a infraestrutura dela.

## Dados:

Os dados foram extraídos dos microdados do "Censo Escolar da Educacação Básica" de 2023, disponíveis em [microdados](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar).

Pegamos uma fatia dos dados, filtrando pelos campos que consideramos relevantes para a nossa análise. A lista dos campos escolhidos se encontra em  [column-filter.txt](./column-filter.txt).

Utilizamos o script [filter-columns.py](./filter-columns.py) com a tabela original "microdados_ed_basica_2023.csv" (disponibilizada via download do arquivo zip no site do censo) e o arquivo [column-filter.txt](./column-filter.txt) (disponível nesse repositório) como input para remover os campos da tabela que não seriam relevantes para nosso trabalho, gerando o arquivo [microdados-filtrados](./microdados-filtrados.csv). Em seguida, utilizamos o script [filter-entries.py](./filter-entries.py) com a tabela filtrada como input para remover as entradas que possuiam dados não preenchidos, gerando o arquivo [microdados-clean](./microdados-clean.csv).

O restante do trabalho foi desenvolvido via Google Colab no link [colab](https://colab.research.google.com/drive/1ErMqAwqiYcbW75WfATq90g5F5r-PYKeu?usp=sharing), utilizando os dados gerados nesse repositório.

