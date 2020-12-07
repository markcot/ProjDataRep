from CompanyDao import companyDao
#print("ok")

# Department test cases
dept1 = {
   'deptID':1,
   'name':'hr',
   'location':'dublin',
   'budget':100000
}

dept2 = {
   'deptID':2,
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
   'empID':100,
   'name':'mary',
   'address':'dublin',
   'salary':60100,
   'dept':1
}

emp2 = {
   'empID':101,
   'name':'tom',
   'address':'wicklow',
   'salary':57000,
   'dept':2
}

emp3 = {
   'empID':102,
   'name':'sarah',
   'address': 'carlow',
   'salary':42000,
   'dept':2
}

emp4 = {
   'empID':102,
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
returnValue = companyDao.findDeptById(dept2['deptID'])
print("find Dept By Id")
print(returnValue)
returnValue = companyDao.findEmpById(emp2['empID'])
print("find Emp By Id")
print(returnValue)

# Update table contents
returnValue = companyDao.updateDept(dept3)
print(returnValue)
returnValue = companyDao.updateEmp(emp4)
print(returnValue)

# Delete table contents
returnValue = companyDao.deleteDept(dept1['deptID'])
print(returnValue)
returnValue = companyDao.deleteDept(dept2['deptID'])
print(returnValue)
returnValue = companyDao.deleteEmp(emp1['empID'])
print(returnValue)
returnValue = companyDao.deleteEmp(emp2['empID'])
print(returnValue)
returnValue = companyDao.deleteEmp(emp3['empID'])
print(returnValue)

# Get all table contents
returnValue = companyDao.getAllDept()
print(returnValue)
returnValue = companyDao.getAllEmp()
print(returnValue)