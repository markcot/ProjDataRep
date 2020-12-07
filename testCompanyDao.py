from CompanyDao import companyDao
#print("ok")


dept1 = {
   # 'deptID' is auto-incremented
   'name':'hr',
   'location':'dublin',
   'budget':100000
}

dept2 = {
   # 'deptID' is auto-incremented
   'name':'sales',
   'location':'kilkenny',
   'budget': 250000
}

dept3 = {
   'name':'it',
   'location':'meath',
   'budget': 350000,
   'deptID':2
}

emp1 = {
   # 'empID' is auto-incremented
   'name':'mary',
   'address':'dublin',
   'salary':60100,
   'dept':1
}

emp2 = {
   # 'empID' is auto-incremented
   'name':'tom',
   'address':'wicklow',
   'salary':57000,
   'dept':2
}

emp3 = {
   # 'empID' is auto-incremented
   'name':'sarah',
   'address': 'carlow',
   'salary':42000,
   'dept':2
}

emp4 = {
   'name':'sue',
   'address': 'dublin',
   'salary':30000,
   'dept':1,
   'empID':3
}

# returnValue = companyDao.createDept(dept1)
# print(returnValue)
# returnValue = companyDao.createDept(dept2)
# print(returnValue)
# returnValue = companyDao.createEmp(emp1)
# print(returnValue)
# returnValue = companyDao.createEmp(emp2)
# print(returnValue)
# returnValue = companyDao.createEmp(emp3)
# print(returnValue)

returnValue = companyDao.getAllDept()
print(returnValue)
returnValue = companyDao.getAllEmp()
print(returnValue)

returnValue = companyDao.findDeptById(2)
print("find Dept By Id")
print(returnValue)
returnValue = companyDao.findEmpById(3)
print("find Emp By Id")
print(returnValue)

returnValue = companyDao.updateDept(dept3)
print(returnValue)
returnValue = companyDao.updateEmp(emp4)
print(returnValue)
