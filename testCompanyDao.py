from CompanyDao import companyDao
#print("ok")

# Department test cases
dept1 = {
   # 'deptID':1, - auto-increment
   'name':'hr',
   'location':'dublin',
   'budget':100000
}

dept2 = {
   # 'deptID':2, - auto-increment
   'name':'sales',
   'location':'kilkenny',
   'budget': 250000
}

dept3 = {
   'deptID':2,
   'name':'it',
   'location':'meath',
   'budget': 350000
}

# Employee test cases
emp1 = {
   # 'empID':1, - auto-increment
   'name':'mary',
   'address':'dublin',
   'salary':60100,
   'dept':1
}

emp2 = {
   # 'empID':2, - auto-increment
   'name':'tom',
   'address':'wicklow',
   'salary':57000,
   'dept':2
}

emp3 = {
   # 'empID':3, - auto-increment
   'name':'sarah',
   'address': 'carlow',
   'salary':42000,
   'dept':2
}

emp4 = {
   'empID':3,
   'name':'sue',
   'address': 'dublin',
   'salary':30000,
   'dept':1
}

# Insert table contents
returnValue = companyDao.createDept(dept1)
print(returnValue)
returnValue = companyDao.createDept(dept2)
print(returnValue)
returnValue = companyDao.createEmp(emp1)
print(returnValue)
returnValue = companyDao.createEmp(emp2)
print(returnValue)
returnValue = companyDao.createEmp(emp3)
print(returnValue)

# Get all table contents
returnValue = companyDao.getAllDept()
print(returnValue)
returnValue = companyDao.getAllEmp()
print(returnValue)

# Get table contents by ID
returnValue = companyDao.findDeptById(2)
print("find Dept By Id")
print(returnValue)
returnValue = companyDao.findEmpById(2)
print("find Emp By Id")
print(returnValue)
returnValue = companyDao.getAllEmpByDept(1)
print("find Emp By Dept Name")
print(returnValue)

# Update table contents
returnValue = companyDao.updateDept(dept3)
print(returnValue)
returnValue = companyDao.updateEmp(emp4)
print(returnValue)

# # Delete table contents
# returnValue = companyDao.deleteDept(1)
# print(returnValue)
# returnValue = companyDao.deleteDept(2)
# print(returnValue)
# returnValue = companyDao.deleteEmp(1)
# print(returnValue)
# returnValue = companyDao.deleteEmp(2)
# print(returnValue)
# returnValue = companyDao.deleteEmp(3)
# print(returnValue)

# Get all table contents
# returnValue = companyDao.getAllDept()
# print(returnValue)
# returnValue = companyDao.getAllEmp()
# print(returnValue)
