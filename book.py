import os
import pandas as pd
import mysql.connector as sqlt
from tabulate import tabulate
con = sqlt.connect(host = "localhost", user = "root", passwd = "Vibhadev72#", database = "library")
cursor = con.cursor()


def book_edit():
    x=int(input("Enter Book ID"))
    qry="select * from book where book_id = {};".format(x)
    cursor.execute(qry)
    r=cursor.fetchone()
    if r:
        y=float(input("Enter New Price"))
        qry="update book set price = {} where book_id = {};".format(y,x)
        cursor.execute(qry)
        con.commit()
        print("Edited Successfully...")
    else:
        print("Wrong Book ID")

def book_delete():
    x=int(input("Enter Book ID"))
    qry="select * from book where book_id = {};".format(x)
    cursor.execute(qry)
    r=cursor.fetchone()
    if r:
        qry="delete from book where book_id = {};".format(x)
        cursor.execute(qry)
        con.commit()
        print("Deleted Successfully...")
    else:
        print("Wrong Book ID")

def book_search():
    x=int(input("Enter Book ID"))
    qry="select * from book where book_id = {};".format(x)
    cursor.execute(qry)
    r=cursor.fetchone()
    if r:
        df = pd.read_sql(qry,con)
        print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
    else:
        print("Wrong Book ID")
        
def book_input():
    try:
        print("This is my input")
        book_id = int(input("Enter Book Id"))
        bname = input("Enter Book Name")
        author = input("Enter author name")
        price = float(input("Enter Price"))
        copies = int(input("Enter No. of Copies"))
        qry = "insert into book values({},'{}','{}',{},{},{});".format(book_id,bname,author,price,copies,copies)
        cursor.execute(qry)
        con.commit()
        print("added successfully...")
    except:
        print("WRONG ENTRY..............")
