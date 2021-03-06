# Company Database Access Object (DAO) for user login and database CRUD operations
# Provides an interface between the flask server and the sql database

# import module and database access configuration file
import mysql.connector
import dbconfig as cfg

# Class object for Database Access Object (DAO)
class CompanyDao:

   # Create database connection pool
   def initConnectToDB(self):
      db = mysql.connector.connect(
         host=cfg.mysql['host'],
         user=cfg.mysql['username'],
         password=cfg.mysql['password'],
         database=cfg.mysql['database'],
         pool_name='my_connection_pool',
         pool_size=5
      )
      return db

   # Get a connection from the pool
   def getConnection(self):
      db = mysql.connector.connect(
         pool_name='my_connection_pool'
      )
      return db

   # Initialise DB connection pool
   def __init__(self):
      db = self.initConnectToDB()
      db.close()

   # Create department, returns deptID of new department
   def createDept(self, dept):
      db = self.getConnection()
      cursor = db.cursor()
      sql = "insert into departments (name, location, budget) values (%s,%s,%s)"
      values = [
         # dept['deptID'], - auto-increment
         dept['name'],
         dept['location'],
         dept['budget']
      ]
      cursor.execute(sql, values)
      db.commit()
      lastRowId = cursor.lastrowid
      db.close()
      return lastRowId
      # return dept['deptID']

   # Create employee, returns empID of new employee
   def createEmp(self, emp):
      db = self.getConnection()
      cursor = db.cursor()
      sql = "insert into employees (name, address, salary, dept) values (%s,%s,%s,%s)"
      values = [
         # emp['empID'], - auto-increment
         emp['name'],
         emp['address'],
         emp['salary'],
         emp['dept']
      ]
      cursor.execute(sql, values)
      db.commit()
      lastRowId = cursor.lastrowid
      db.close()
      return lastRowId
      # return emp['empID']

   # Create user, returns userID of new user
   def createUser(self, u):
      db = self.getConnection()
      cursor = db.cursor()
      sql = "insert into users (name, password) values (%s,%s)"
      values = [
         # u['userID'], - auto-increment
         u['name'],
         u['password'],
      ]
      cursor.execute(sql, values)
      db.commit()
      lastRowId = cursor.lastrowid
      db.close()
      return lastRowId
      # return u['userID']

   # Return info on all departments
   def getAllDept(self):
      db = self.getConnection()
      cursor = db.cursor()
      sql = 'select * from departments'
      cursor.execute(sql)
      results = cursor.fetchall()
      returnArray = []
      # print(results)
      for result in results:
         resultAsDict = self.convertDeptToDict(result)
         returnArray.append(resultAsDict)
      db.close()
      return returnArray

   # Return info on all employees
   def getAllEmp(self):
      db = self.getConnection()
      cursor = db.cursor()
      sql = 'select * from employees'
      cursor.execute(sql)
      results = cursor.fetchall()
      returnArray = []
      # print(results)
      for result in results:
         resultAsDict = self.convertEmpToDict(result)
         returnArray.append(resultAsDict)
      db.close()
      return returnArray

   # Return info on all users
   def getAllUser(self):
      db = self.getConnection()
      cursor = db.cursor()
      sql = 'select * from users'
      cursor.execute(sql)
      results = cursor.fetchall()
      returnArray = []
      # print(results)
      for result in results:
         resultAsDict = self.convertUserToDict(result)
         # print(result)
         returnArray.append(resultAsDict)
      db.close()
      return returnArray

   # Return info on department for given deptID
   def findDeptById(self, deptID):
      db = self.getConnection()
      cursor = db.cursor()
      sql = 'select * from departments where deptID = %s'
      values = [deptID]
      cursor.execute(sql, values)
      result = cursor.fetchone()
      dept = self.convertDeptToDict(result)
      db.close()
      return dept

   # Return info on employee for given empID
   def findEmpById(self, empID):
      db = self.getConnection()
      cursor = db.cursor()
      sql = 'select * from employees where empID = %s'
      values = [empID]
      cursor.execute(sql, values)
      result = cursor.fetchone()
      emp = self.convertEmpToDict(result)
      db.close()
      return emp

   # Return info on user for given userID
   def findUserByID(self, userID):
      db = self.getConnection()
      cursor = db.cursor()
      sql = 'select * from users where userID = %s'
      values = [userID]
      cursor.execute(sql, values)
      result = cursor.fetchone()
      u = self.convertUserToDict(result)
      db.close()
      return u

   # Return info on all employees associated with a given department deptID
   def getAllEmpByDept(self, deptID):
      db = self.getConnection()
      cursor = db.cursor()
      sql = 'select * from employees where dept = %s;'
      values = [deptID]
      cursor.execute(sql, values)
      results = cursor.fetchall()
      returnArray = []
      # print(results)
      for result in results:
         resultAsDict = self.convertEmpToDict(result)
         returnArray.append(resultAsDict)
      db.close()
      return returnArray

   # Update department info for given deptID, returns updated info
   def updateDept(self, dept):
      db = self.getConnection()
      cursor = db.cursor()
      sql = "update departments set name = %s, location = %s, budget = %s where deptID = %s"
      values = [
         dept['name'],
         dept['location'],
         dept['budget'],
         dept['deptID']
      ]
      cursor.execute(sql, values)
      db.commit()
      db.close()
      return dept

   # Update employee info for given empID, returns updated info
   def updateEmp(self, emp):
      db = self.getConnection()
      cursor = db.cursor()
      sql = "update employees set name = %s, address = %s, salary = %s, dept = %s where empID = %s"
      values = [
         emp['name'],
         emp['address'],
         emp['salary'],
         emp['dept'],
         emp['empID']
      ]
      cursor.execute(sql, values)
      db.commit()
      db.close()
      return emp

   # Update user info for given userID, returns updated info
   def updateUser(self, u):
      db = self.getConnection()
      cursor = db.cursor()
      sql = "update users set name = %s, password = %s where userID = %s"
      values = [
         u['name'],
         u['password'],
         u['userID']
      ]
      cursor.execute(sql, values)
      db.commit()
      db.close()
      return u

   # Delete department for given deptID, returns empty dictionary/JSON
   def deleteDept(self, deptID):
      db = self.getConnection()
      cursor = db.cursor()
      sql = 'delete from departments where deptID = %s'
      values = [deptID]
      cursor.execute(sql, values)
      db.commit()
      db.close()
      return {}

   # Delete employee for given empID, returns empty dictionary/JSON
   def deleteEmp(self, empID):
      db = self.getConnection()
      cursor = db.cursor()
      sql = 'delete from employees where empID = %s'
      values = [empID]
      cursor.execute(sql, values)
      db.commit()
      db.close()
      return {}

   # Delete user for given userID, returns empty dictionary/JSON
   def deleteUser(self, userID):
      db = self.getConnection()
      cursor = db.cursor()
      sql = 'delete from users where userID = %s'
      values = [userID]
      cursor.execute(sql, values)
      db.commit()
      db.close()
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

   # Function to convert user into Dictionary/JSON
   def convertUserToDict(self, result):
      colnames = ['userID', 'name', 'password']
      u = {}
      if result:
         for i, colName in enumerate(colnames):
            value = result[i]
            u[colName] = value
      return u

# Create instance of the DOA class
companyDao = CompanyDao()