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
         # 'deptID' is auto-incremented
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
         # 'empID' is auto-incremented
         emp['name'],
         emp['address'],
         emp['salary'],
         emp['dept']
      ]
      cursor.execute(sql, values)
      self.db.commit()
      return cursor.lastrowid

   # Return info on all departments
   def getAllDept(self):
      cursor = self.db.cursor()
      sql = 'select * from department'
      cursor.execute(sql)
      results = cursor.fetchall()
      returnArray = []
      # print(results)
      for result in results:
         resultAsDict = self.convertDeptToDict(result)
         returnArray.append(resultAsDict)
      return returnArray

   # Return info on all employees
   def getAllEmp(self):
      cursor = self.db.cursor()
      sql = 'select * from employee'
      cursor.execute(sql)
      results = cursor.fetchall()
      returnArray = []
      # print(results)
      for result in results:
         resultAsDict = self.convertEmpToDict(result)
         returnArray.append(resultAsDict)
      return returnArray

   # Return info on department for given deptID
   def findDeptById(self, deptID):
      cursor = self.db.cursor()
      sql = 'select * from department where deptID = %s'
      values = [ deptID ]
      cursor.execute(sql, values)
      result = cursor.fetchone()
      return self.convertDeptToDict(result)

   # Return info on employee for given empID
   def findEmpById(self, empID):
      cursor = self.db.cursor()
      sql = 'select * from employee where empID = %s'
      values = [ empID ]
      cursor.execute(sql, values)
      result = cursor.fetchone()
      return self.convertEmpToDict(result)





   # Function to convert department into Dictionary/JSON
   def convertDeptToDict(self, result):
      colnames = ['deptID', 'name', 'location', 'budget']
      dept = {}
      if result:
         for i , colName in enumerate(colnames):
               value = result[i]
               dept[colName] = value
      return dept

   # Function to convert employee into Dictionary/JSON
   def convertEmpToDict(self, result):
      colnames = ['empID', 'name', 'address', 'salary', 'dept']
      emp = {}
      if result:
         for i, colName in enumerate(colnames):
             value = result[i]
             emp[colName] = value
      return emp

companyDao = CompanyDao()
