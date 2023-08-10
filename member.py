import book as b
import os
import pandas as pd
import mysql.connector as sqlt
from tabulate import tabulate
con = sqlt.connect(host = "localhost", user = "root", passwd = "Vibhadev72#", database = "library")
cursor = con.cursor()

def member_input():
    try:
        memberid = int(input("Enter MemberID"))
        mname = input("Enter Member Name")
        madd = input("Enter Member Address")
        phone = input("Enter Phone No")
        qry = "insert into member values({},'{}','{}','{}')".format(memberid, mname, madd, phone)
        cursor.execute(qry)
        con.commit()
    except:
        print("Wrong Entry.........")
    #cursor.close()
    
def member_output():
    qry = "select * from member;"
    df=pd.read_sql(qry,con)
    #cursor.execute(qry)
    #x=cursor.fetchall()
    #print(x)
    #print(df.to_string(index=False))
    print(tabulate(df , headers = 'keys',tablefmt = 'psql', showindex= False))
    print()
    
def member_edit():
    x=int(input("Enter Member ID"))
    qry="select * from Member where memberid = {};".format(x)
    cursor.execute(qry)
    r=cursor.fetchone()
    #con.commit()
    if r:
        #print("Exist")
        add = input("Enter new Address")
        qry = "update member set madd = '{}' where memberid = {};".format(add,x)
        cursor.execute(qry)
        con.commit()
        print("updated")
    else:
        print("Wrong MemberID")
    #cursor.close()

def member_delete():
    x=int(input("Enter Member ID"))
    qry="select * from member where memberid = {};".format(x)
    cursor.execute(qry)
    r=cursor.fetchone()
    #con.commit()
    if r:
        #print("Exist")
        ch = input("Are you sure you want to delete y/n")
        if ch == 'y':
            qry='delete from member where memberid = {};'.format(x)
            cursor.execute(qry)
            con.commit()

def member_search():
    x=int(input("Enter Member ID"))
    qry="select * from member where memberid = {};".format(x)
    cursor.execute(qry)
    r=cursor.fetchone()
    if r:
        df = pd.read_sql(qry,con)
        print(tabulate(df, headers = 'keys', tablefmt = 'psql', showindex = False))
    else:
        print("Wrong Member ID")
