import sqlite3
import os
import glob
#initilize connection with existing database or create one...
def init_db(db_name):
    print('\n***initializing database -->'+db_name+'***\n')
    name=db_name
    global con
    con= sqlite3.connect(name)
    global db
    db= con.cursor() #creating cursor object to run queries...
    print('***connection success ***\n')
#create table directly instead of writing queries...
def create_table(table_name):
    table=table_name
    print('\n***accessing'+table+'***\n')
    global coloumn_name 
    coloumn_name =input("coloumn_names :")
    db.execute('DROP TABLE IF EXISTS '+table)
    db.execute('''CREATE TABLE '''+table+'''('''+coloumn_name+''')''')
    print(table+' created successfully \n')
    con.commit()
#shows inserted data in table
def show_table(table_name):    
    t=table_name
    #c=db.execute("SELECT * FROM "+t).fetchall()
    #print(c)
    for row in db.execute("SELECT * FROM "+t):
        print(row)
        print('\n')
#insert elements to table....
def insert(table_name):
    t=table_name
    v=input('enter values:')
    db.execute("insert into "+t+" values("+v+")")
    con.commit()
#drop existing table....    
def drop_table(table_name):
    table=table_name
    db.execute('DROP TABLE '+table)
    con.commit()
    print(table+'removed')
#showing files with specified extensions.....
def show_db():
    print('| AVAILABLE DATABASES |')
    for x in glob.glob('*.db'):
        print(x)
    for x in glob.glob('*.sqlite'):
        print(x)
    #add new extension of database 
    #for x in glob.glob('*.database extensions')
    #    print(x)
    
#manually run script of queries written in file schema.sql   .......
def run_script():
    f=open('schema.sql', 'r+')
    db.executescript(f.read())
    con.commit()
    f.close()
#dont forget to commit changes ........-->con.commit()<--..........
    



        
 
