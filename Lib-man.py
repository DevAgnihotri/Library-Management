import book as b
import member as m
import report as r
import transaction as t
import os
import pandas as pd
import mysql.connector as sqlt
import matplotlib.pyplot as plt
from tabulate import tabulate
con = sqlt.connect(host = "localhost", user = "root", passwd = "Vibhadev72#", database = "library")
cursor = con.cursor()

# --------------------------------- -------------------------------------------------------------------------

# ------------------------------------------------- Book ---------------------------------------------

#-------------------------------------------------------------------------------------------

# ---------------------------------------- [] -----------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------------------------------
while(True):
    print("H"*120)
    print("\t\t\t\t\t\t\t------------Library Mangement System--------------\n")
    print("\t\t\t\t\t\t\t\tEnter Your Choice\n\t\t\t\t\t\t\t\t1.Book Details\n\t\t\t\t\t\t\t\t2.Member Details\n\t\t\t\t\t\t\t\t3.Transaction\n\t\t\t\t\t\t\t\t4.Report\n\t\t\t\t\t\t\t\t5.Exit")
    choice = int(input())
    if choice == 1:
        while(True):
            print("\t\t\t\t\t\t\t\tEnter your choice\n\t\t\t\t\t\t\t\t1. Add book details\n\t\t\t\t\t\t\t\t2. Edit Book Details\n\t\t\t\t\t\t\t\t3. Delete a book\n\t\t\t\t\t\t\t\t4. Search a book\n\t\t\t\t\t\t\t\t5. Back to main menu")
            ch=int(input())
            if ch == 1:
                b.book_input()
            elif ch == 2:
                b.book_edit()
            elif ch == 3:
                b.book_delete()
            elif ch == 4:
                b.book_search()
            elif ch == 5:
                break
    elif choice == 2:
       while(True):
            print("\t\t\t\t\t\t\t\tEnter your choice\n\t\t\t\t\t\t\t\t1. Add Member details\n\t\t\t\t\t\t\t\t2. Edit member Details\n\t\t\t\t\t\t\t\t3. Delete a Member\n\t\t\t\t\t\t\t\t4. Search a member\n\t\t\t\t\t\t\t\t5. Back to main menu")
            ch=int(input())
            if ch == 1:
                m.member_input()
            elif ch == 2:
                m.member_edit()
            elif ch == 3:
                m.member_delete()
            elif ch == 4:
                m.member_search()
            elif ch == 5:
                break
    elif choice == 3:
        while(True):
            print("\t\t\t\t\t\t\t\tEnter your choice\n\t\t\t\t\t\t\t\t1. Issue Book\n\t\t\t\t\t\t\t\t2. Return Book\n\t\t\t\t\t\t\t\t3. Back to main menu")
            ch=int(input())
            if ch == 1:
                t.book_issue()
            elif ch == 2:
                t.book_return()
            elif ch == 3:
                break
    elif choice == 4:
        while(True):
            print("\t\t\t\t\t\t\t\tEnter your choice\n\t\t\t\t\t\t\t\t1. Book details\n\t\t\t\t\t\t\t\t2. Member Details\n\t\t\t\t\t\t\t\t3. Issue details\n\t\t\t\t\t\t\t\t4. Return Details\n\t\t\t\t\t\t\t\t5. Best reading Book(Chart)\n\t\t\t\t\t\t\t\t6. Back to main menu")
            ch=int(input())
            if ch == 1:
                r.book_output()
            elif ch == 2:
                r.member_output()
            elif ch == 3:
                r.issue_output()
            elif ch == 4:
                r.return_output()
            elif ch == 5:
                r.col_chart()
            elif ch == 6:
                break
    elif choice == 5:
        break
        
