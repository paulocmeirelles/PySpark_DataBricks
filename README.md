# Python - PySpark - Databricks

## SOBRE

- Este projecto visa resolver o problema proposto pela empresa RNP

## REQUISITOS

- python 3.10
- conta na AWS e uma conta na extensão Databricks
- pip instalado

## REPOSITORIO

.
└── PYTHON_DATATREATMENT
├── main
│ ├── **init**.py
│ ├── question1.py
│ ├── question2.py
│ ├── question3.py
│ ├── regex_helper.py
├── question1_pandas.parquet
├── question1_pyspark.parquet
├── question2_pandas.parquet
├── question2_pyspark.parquet
├── question3_pandas.parquet
├── question3_pyspark.parquet
├── requirements.txt
└── Test_RNP_Notebook.ipynb

## PASSOS

Primeiro, clone o projeto do git caso for executar a solução em python. Caso contrário, copie ou baixe o notebook "Test_RNP_Notebook.ipynb" e importe para o notebook do Databricks.

Crie um arquivo .env e nele coloque as credenciais para a conexão com o banco de dados postgresql. Utilize o arquivo setting.env como base.

```
python3 -m venv venv
```

```
source ./venv/bin/activate
```

```
pip install -r requirements.txt
```

Dentro da pasta main execute o script das questões 1, 2 e 3 para obter as respostas dos problemas. Execute-os apenas com o comandos abaixo.

```
python3 ./main/question1.py
```

```
python3 ./main/question2.py
```

```
python3 ./main/question3.py
```

### P.S.

1. Os arquivos em .parquet foram obtidos em formato delta através do Databricks notebook.
2. Para os arquivos .parquet das tabelas pandas, foram executados também no mesmo notebook com os mesmos comandos feitos nos scripts .py, a diferença é que na requisição das tabelas foram convertidas com a função "toPandas()" para que eu pudesse trabalhar com pandas e no final eu converti novamente para spark table com a função "spark.createDataFrame()".
3. Os comandos acima não estão no notebook mais por uma questão de estética, logo eu separei a solução usando o pyspark table para o notebook e a com pandas para o desenvolvimento local.
4. Ecommerce db.pdf é o esquema do banco de dados do exercício.
