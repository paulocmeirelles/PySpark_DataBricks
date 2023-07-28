# Python - PySpark - Databricks

## SOBRE

- Este projecto visa resolver o problema propostos, assim como mostrar como manejar dados com o databricks utilizando pyspark e python pandas. Salvando as respostas em formato delta.

## REQUISITOS

- python 3.10
- conta na AWS e uma conta na extensão Databricks
- pip instalado

## REPOSITORIO

.
└── PYTHON_DATATREATMENT<br />
├── main<br />
│ ├── **init**.py<br />
│ ├── question1.py<br />
│ ├── question2.py<br />
│ ├── question3.py<br />
│ ├── regex_helper.py<br />
├── question1_pandas.parquet<br />
├── question1_pyspark.parquet<br />
├── question2_pandas.parquet<br />
├── question2_pyspark.parquet<br />
├── question3_pandas.parquet<br />
├── question3_pyspark.parquet<br />
├── requirements.txt<br />
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
