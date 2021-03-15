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

## Add  import statement to python script to use SQLite3; and csv to upload record for you tables.
- import sqlite3, csv
## Use the function sqlite.connect to create a file myhospitaldb with sqlite3.
- sqlite_connection = sqlite3.connect ('MyHospital.db')
## Create a cursor object; this is needed to execute any operation to the db. i.e creating tables, updating and even print the db vesion.
-conn = sqlite_connection.cursor()
## import csv file using "with open" to populate your table and capture the full path where your CSV file is stored.
- with open ('C:\python\Assignment\sqlite\Hospital.csv', 'r')
## Define a fucntion to join the two tables:
-def inner_join():
#use the hospital_id identifier to only display the records common in the two tables.
- ON Hospital.Hospital_id = Doctor.Hospital_id; ''')
 ## Call the function to display the result of the above methods
- inner_join()

