from db import engine
import pandas as pd
from regex_helper import mask_local_part

def question_3():
    df_offices = pd.read_sql_query("""SELECT * FROM offices;""", engine)
    df_employees = pd.read_sql_query("""SELECT * FROM employees;""", engine)

    df_question_3 = pd.merge(df_offices,df_employees,how="inner", on='office_code')
    df_question_3 = df_question_3[df_question_3['country']=='Japan'].loc[:,['first_name','last_name','email']]
    df_question_3['email'] = df_question_3['email'].apply(lambda string: mask_local_part(string))
    print(df_question_3)


if __name__ == '__main__':
    question_3()