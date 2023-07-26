import pandas as pd
from db import engine

def question_1():
    df_orders = pd.read_sql_query("""SELECT * FROM orders;""", engine)
    df_orderdetails = pd.read_sql_query("""SELECT * FROM orderdetails;""", engine)
    df_customers = pd.read_sql_query("""SELECT * FROM customers;""", engine)

    df_question_1 = pd.merge(df_orders,df_orderdetails,how="inner", on='order_number')
    df_question_1 = pd.merge(df_question_1,df_customers,how="inner", on='customer_number')
    df_question_1 = df_question_1[df_question_1['status']=='Cancelled']
    print(df_question_1.loc[:,['country','quantity_ordered']].groupby(by='country').sum().sort_values(by='quantity_ordered', ascending=False))


if __name__ == '__main__':
    question_1()
