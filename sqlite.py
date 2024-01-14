import sqlite3

## connect to the SQLlite database
connection=sqlite3.connect("student4.db")

#create a cursor object to insert record, create table

cursor=connection.cursor()

##create the table

table_info="""
Create table STUDENT4(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25));

"""
cursor.execute(table_info)

#Insert some records

cursor.execute('''Insert Into STUDENT4 Values('Kusum','Data Science','A')''')
cursor.execute('''Insert Into STUDENT4 Values('Kusu','Data Science','B')''')
cursor.execute('''Insert Into STUDENT4 Values('Komal','Devops','C')''')
cursor.execute('''Insert Into STUDENT4 Values('Ram','Data Science','A')''')
cursor.execute('''Insert Into STUDENT4 Values('Sohan','Data Analystics','D')''')
cursor.execute('''Insert Into STUDENT4 Values('Kushi','Data Science','A')''')



#Display all the records
print("The inserted records are")
data=cursor.execute('''Select * from STUDENT4''')
for row in data:
    print(row)

#Commit your changes in the database
connection.commit()
connection.close()