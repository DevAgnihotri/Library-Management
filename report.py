import os
import pandas as pd
import mysql.connector as sqlt
from tabulate import tabulate
import matplotlib.pyplot as plt
con = sqlt.connect(host = "localhost", user = "root", passwd = "Vibhadev72#", database = "library")
cursor = con.cursor()

def book_output():
    df = pd.read_sql("select * from book",con)
    print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))

def return_output():
    df = pd.read_sql("select * from returns",con)
    print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))

def issue_output():
    df = pd.read_sql("select * from issue",con)
    print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))

def member_output():
    qry = "select * from member;"
    df=pd.read_sql(qry,con)
    #cursor.execute(qry)
    #x=cursor.fetchall()
    #print(x)
    #print(df.to_string(index=False))
    print(tabulate(df , headers = 'keys',tablefmt = 'psql', showindex= False))
    print()

def col_chart():
    q = "select book_id, count(copies) as totalcopies from issue group by book_id;"
    df=pd.read_sql(q,con)
    print(df)
    plt.bar(df.book_id, df.totalcopies)
    plt.xlabel("BookiD")
    plt.ylabel("Copies Issued")
    plt.title("Most read Books")
    plt.xticks(df.book_id)
    plt.show()
