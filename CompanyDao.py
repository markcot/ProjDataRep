import mysql.connector
import dbconfig as cfg

class CompanyDao:
   db = ""

   # Create database connection
   def connectToDB(self):
      self.db = mysql.connector.connect(
          host=cfg.mysql['host'],
          user=cfg.mysql['username'],
          password=cfg.mysql['password'],
          database=cfg.mysql['database']
      )
      #print ("connection made")

   def __init__(self):
      self.connectToDB()

   # check if connection to DB is made. If not connected make connection
   def getCursor(self):
      if not self.db.is_connected():
         self.connectToDB()
      return self.db.cursor()

   # Create department
   def createDept(self, dept):
      cursor = self.getCursor()
      sql = "insert into departments (name, location, budget) values (%s,%s,%s)"
      values = [
          # dept['deptID'], - auto-increment
          dept['name'],
          dept['location'],
          dept['budget']
      ]
      cursor.execute(sql, values)
      self.db.commit()
      lastRowId = cursor.lastrowid
      cursor.close()
      return lastRowId
      # return dept['deptID']

   # Create employee
   def createEmp(self, emp):
      cursor = self.getCursor()
      sql = "insert into employees (name, address, salary, dept) values (%s,%s,%s,%s)"
      values = [
          # emp['empID'], - auto-increment
          emp['name'],
          emp['address'],
          emp['salary'],
          emp['dept']
      ]
      cursor.execute(sql, values)
      self.db.commit()
      lastRowId = cursor.lastrowid
      cursor.close()
      return lastRowId
      # return emp['empID']

   # Return info on all departments
   def getAllDept(self):
      cursor = self.getCursor()
      sql = 'select * from departments'
      cursor.execute(sql)
      results = cursor.fetchall()
      returnArray = []
      # print(results)
      for result in results:
         resultAsDict = self.convertDeptToDict(result)
         returnArray.append(resultAsDict)
      cursor.close()
      return returnArray

   # Return info on all employees
   def getAllEmp(self):
      cursor = self.getCursor()
      sql = 'select * from employees'
      cursor.execute(sql)
      results = cursor.fetchall()
      returnArray = []
      # print(results)
      for result in results:
         resultAsDict = self.convertEmpToDict(result)
         returnArray.append(resultAsDict)
      cursor.close()
      return returnArray

   # Return info on department for given deptID
   def findDeptById(self, deptID):
      cursor = self.getCursor()
      sql = 'select * from departments where deptID = %s'
      values = [deptID]
      cursor.execute(sql, values)
      result = cursor.fetchone()
      dept = self.convertDeptToDict(result)
      cursor.close()
      return dept

   # Return info on employee for given empID
   def findEmpById(self, empID):
      cursor = self.getCursor()
      sql = 'select * from employees where empID = %s'
      values = [empID]
      cursor.execute(sql, values)
      result = cursor.fetchone()
      emp = self.convertEmpToDict(result)
      cursor.close()
      return emp

   # Return info on all employees from a given department ID
   def getAllEmpByDept(self, deptID):
      cursor = self.getCursor()
      sql = 'select * from employees where dept = %s;'
      values = [deptID]
      cursor.execute(sql, values)
      results = cursor.fetchall()
      returnArray = []
      # print(results)
      for result in results:
         resultAsDict = self.convertEmpToDict(result)
         returnArray.append(resultAsDict)
      cursor.close()
      return returnArray

   # Update department info for given deptID
   def updateDept(self, dept):
      cursor = self.getCursor()
      sql = "update departments set name = %s, location = %s, budget = %s where deptID = %s"
      values = [
          dept['name'],
          dept['location'],
          dept['budget'],
          dept['deptID']
      ]
      cursor.execute(sql, values)
      self.db.commit()
      cursor.close()
      return dept

   # Update employee info for given empID
   def updateEmp(self, emp):
      cursor = self.getCursor()
      sql = "update employees set name = %s, address = %s, salary = %s, dept = %s where empID = %s"
      values = [
          emp['name'],
          emp['address'],
          emp['salary'],
          emp['dept'],
          emp['empID']
      ]
      cursor.execute(sql, values)
      self.db.commit()
      cursor.close()
      return emp

   # Delete department for given deptID
   def deleteDept(self, deptID):
      cursor = self.getCursor()
      sql = 'delete from departments where deptID = %s'
      values = [deptID]
      cursor.execute(sql, values)
      self.db.commit()
      cursor.close()
      return {}

   # Delete employee for given empID
   def deleteEmp(self, empID):
      cursor = self.getCursor()
      sql = 'delete from employees where empID = %s'
      values = [empID]
      cursor.execute(sql, values)
      self.db.commit()
      cursor.close()
      return {}

   # Function to convert department into Dictionary/JSON
   def convertDeptToDict(self, result):
      colnames = ['deptID', 'name', 'location', 'budget']
      dept = {}
      if result:
         for i, colName in enumerate(colnames):
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
