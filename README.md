# Myhospital
#Create a SQLite database connection to a database that resides in the memory - Show your python code and the table structure. 

#  Write a Python program to create a SQLite database and connect with the database and print the version of the SQLite database - Show your Python code.

#Using Python and SQLite, create two Tables a: Hospital and b: Doctors

#a) Hospital:
    Hospital_id
    Hospital_Name
    Bed-count

#b) Doctor:
    Doctor_id
    Doctor_Name
    Hospital_id
    Date_joined
    Speciality
    Salary
    Experience

#Join these two tables by Hospital Id 

## add  import statement to our python script to use SQLite3; and csv to upload record for you tables.
- import sqlite3, csv
## use the function sqlite.connect to create a file myhospitaldb with sqlite3.
- sqlite_connection = sqlite3.connect ('MyHospital.db')
## ceate a cursor object; this is needed to execute any opeation to the db. i.e creating tables, updating and even pint the db vesion.
-conn = sqlite_connection.cursor()
## import 
