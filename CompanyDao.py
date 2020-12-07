import mysql.connector
import dbconfig as cfg
from mysql.connector import cursor

class CompanyDao:
   db = ""
   
   # Create database connection
   def __init__(self):
      self.db = mysql.connector.connect(
         host=cfg.mysql['host'],
         user=cfg.mysql['username'],
         password=cfg.mysql['password'],
         database=cfg.mysql['database']
      )
      #print ("connection made")

   # Create department
   def createDept(self, dept):
      cursor = self.db.cursor()
      sql = "insert into department (name, location, budget) values (%s,%s,%s)"
      values = [
         # deptID is auto-incremented
         dept['name'],
         dept['location'],
         dept['budget']
      ]
      cursor.execute(sql, values)
      self.db.commit()
      return cursor.lastrowid

   # Create employee
   def createEmp(self, emp):
      cursor = self.db.cursor()
      sql = "insert into employee (name, address, salary, dept) values (%s,%s,%s,%s)"
      values = [
         # empID is auto-incremented
          emp['name'],
          emp['address'],
          emp['salary'],
          emp['dept']
      ]
      cursor.execute(sql, values)
      self.db.commit()
      return cursor.lastrowid

companyDao = CompanyDao()
