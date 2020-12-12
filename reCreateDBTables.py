import mysql.connector
import dbconfig as cfg

ask = input("Have you sure you want to delete the DB tables (y/n): ")

if ask == "y":
   # Create database connection
   db = mysql.connector.connect(
      host=cfg.mysql['host'],
      user=cfg.mysql['username'],
      password=cfg.mysql['password'],
      database=cfg.mysql['database']
   )
   # print ("connection made")

   # Delete employees table
   cursor = db.cursor()
   sql="drop table employees"
   cursor.execute(sql)
   db.commit()
   print("employees table delete done")

   # Delete departments table
   cursor = db.cursor()
   sql="drop table departments"
   cursor.execute(sql)
   db.commit()
   print("departments table delete done")

   # recreate departments table
   cursor = db.cursor()
   sql ="""CREATE TABLE departments(
      deptID INT NOT NULL AUTO_INCREMENT,
      name VARCHAR(255) DEFAULT NULL,
      location varchar(255) DEFAULT NULL,
      budget INT DEFAULT NULL,
      PRIMARY KEY(deptID)
      )"""
   cursor.execute(sql)
   print("departments table creation done")

   # recreate employees table
   cursor = db.cursor()
   sql = """CREATE TABLE employees(
      empID INT NOT NULL AUTO_INCREMENT,
      name VARCHAR(255) DEFAULT NULL,
      address VARCHAR(255) DEFAULT NULL,
      salary INT DEFAULT NULL,
      dept INT DEFAULT NULL,
      PRIMARY KEY (empID),
      CONSTRAINT FK_deptEmp
         FOREIGN KEY (dept)
         REFERENCES departments(deptID)
         ON DELETE RESTRICT
      )"""
   cursor.execute(sql)
   print("employees table creation done")

   cursor.close()
   db.close()
else:
   print("DB tables not deleted")
