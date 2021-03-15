#!/usr/bin/env python
# coding: utf-8


import sqlite3, csv
sqlite_connection = sqlite3.connect ('MyHospital.db')

print ("MyHospital Database Created successfully!")



# Get the cursor object
conn = sqlite_connection.cursor()
#sqlite DB version
version = conn.execute ('select sqlite_version();')
print ('the sqlite Db version is: ', version.fetchall(), "\n")



# create hospital table
conn.execute('''CREATE TABLE IF NOT EXISTS Hospital
            (Hospital_id INT PRIMARY KEY NOT NULL,
             Hospital_Name TEXT NOT NULL,
             Bed_count INT NOT NULL);''')

# display table
content = conn.execute("PRAGMA table_info('Hospital');")
print ("\t Hospital Table:\n -------------------------------------")
print(content.fetchall(), '\n')




#import csv file
with open ('C:\python\Assignment\sqlite\Hospital.csv', 'r') as hosp_csv:
    reader=csv.reader (hosp_csv)
    for row in reader:
        conn.execute("INSERT OR REPLACE INTO Hospital VALUES (?, ?, ?);",row)
        sqlite_connection.commit()
print("rows added:")





# create Doctor's table
conn.execute('''CREATE TABLE IF NOT EXISTS Doctor
            (Doctor_id INT PRIMARY KEY NOT NULL,
             Doctor_Name TEXT NOT NULL,
             Hospital_id INT NOT NULL,
             Date_joined TEXT NOT NULL,
             Speciality TEXT NOT NULL,
             Salary REAL NOT NULL,
             Experience VARCHAR(10) NOT NULL,
             FOREIGN KEY (Hospital_id) References Hospital(Hospital_id) );''')

# display tables
cont = conn.execute("PRAGMA table_info('Doctor');")
print ("\t Doctor Table:\n \t---------------")
print(cont.fetchall(), '\n')



#import csv file
with open ('C:\python\Assignment\sqlite\Doctor.csv', 'r') as doc_csv:
    reader=csv.reader (doc_csv)
    for row in reader:
        conn.execute("INSERT OR REPLACE INTO Doctor VALUES (?, ?, ?, ?, ?,?, ?);",row)
        sqlite_connection.commit()
print("rows added:")


# define function to join the two table

def inner_join():
    joined = conn.execute (''' SELECT * 
                                FROM Doctor 
                                INNER JOIN Hospital 
                                ON Hospital.Hospital_id = Doctor.Hospital_id; ''')
    # show content
    print("\t\t inner join result:\n \t\t ------------------\n")
    for i in joined.fetchall():
        print(i)
# call the method
inner_join()
#close the cursor connection
conn.close()





