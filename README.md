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
## create a cursor object; this is needed to execute any operation to the db. i.e creating tables, updating and even print the db vesion.
-conn = sqlite_connection.cursor()
## import csv file using "with open" to populate your table and capture the full path where your CSV file is stored.
- with open ('C:\python\Assignment\sqlite\Hospital.csv', 'r')

