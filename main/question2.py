import pandas as pd
from db import engine

def question_2():
    df_orders = pd.read_sql_query("""SELECT * FROM orders;""", engine)
    df_orderdetails = pd.read_sql_query("""SELECT * FROM orderdetails;""", engine)
    df_products = pd.read_sql_query("""SELECT * FROM products;""", engine)

    df_question_2 = pd.merge(df_orders,df_orderdetails,how="inner", on='order_number')
    df_question_2 = pd.merge(df_question_2,df_products,how="inner", on='product_code')
    df_question_2['order_date'] = pd.to_datetime(df_question_2['order_date'], format='%Y-%m-%d')
    df_question_2 = df_question_2[(df_question_2['status']=='Shipped') & (df_question_2['order_date']>'2005-01-01') & (df_question_2['order_date']<'2005-12-31')]
    # Just to know which item is the best seller
    grouped =  df_question_2.loc[:,['product_code','product_name','price_each','quantity_ordered']].groupby(by='product_code').sum().sort_values(by='quantity_ordered', ascending=False)

    df_question_2 = df_question_2[df_question_2['product_code']=='S18_3232'].loc[:,['product_code','product_name','price_each','quantity_ordered']]
    df_question_2['revenue_for_item'] = df_question_2['price_each']*df_question_2['quantity_ordered']
    df_question_2['result'] = df_question_2['quantity_ordered']*df_question_2['price_each']
    result = df_question_2['result'].sum()
    print(result)

if __name__ == '__main__':
    question_2()