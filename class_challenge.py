def Menu():
    print("Main Menu:")
    print("1. Insert a record")
    print("2. Read all records")
    print("3. Exit")
    selection=input("Input your choice 1, 2 or 3 (no other selection are valid): ")
    if selection=="1":
        insertStuff()
    elif selection=="2":
        readStuff()
    elif selection=="3":
        conn.close
        exit(1)
    else:
        Menu()

    

def insertStuff():
    myDate=input("Input date:")
    myTX=input("Transaction type:")
    mySymbol=input("Input ticker symbol:")
    myQty=float(input("Enter the quantity:"))
    myPrice=float(input("Enter price:"))
    data.execute('''INSERT INTO stocks 
                 (myDate, myTX, mySymbol, myQty, myPrice) VALUES(?,?,?,?,?)''',(myDate, myTX,mySymbol,myQty,myPrice))
    conn.commit()

def readStuff():
    data.execute('SELECT * FROM stocks')
    for row in data.fetchall():
        print(row)

import sqlite3
selection="Null"
conn=sqlite3.connect('example.db')
data=conn.cursor()
data.execute('''create table if not exists stocks 
             (myDate text, myTX text, mySymbol text, myQty real, myPrice real)''')
conn.commit()
Menu()
conn.close()
