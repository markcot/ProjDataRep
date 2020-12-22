from flask import Flask, url_for, request, redirect, abort, jsonify
from CompanyDao import companyDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')

# Root route
# curl http://127.0.0.1:5000/
# @app.route('/')
# def index():
#    return app.send_static_file('index.html')
@app.route('/')
def login():
   return app.send_static_file('login.html')

#get all departments route
# curl http://127.0.0.1:5000/departments
@app.route('/departments')
def getAllDept():
   return jsonify(companyDao.getAllDept())

#get all employees route
# curl http://127.0.0.1:5000/employees
@app.route('/employees')
def getAllEmp():
   return jsonify(companyDao.getAllEmp())

#get all users route (userID and name only)
# curl http://127.0.0.1:5000/users
@app.route('/u')
def getAllUser():
   return jsonify(companyDao.getAllUser())

# find By department id route
# curl http://127.0.0.1:5000/departments/1
@app.route('/departments/<int:deptID>')
def findDeptById(deptID):
   return jsonify(companyDao.findDeptById(deptID))

# find By employee id route
# curl http://127.0.0.1:5000/employees/1
@app.route('/employees/<int:empID>')
def findEmpById(empID):
   return jsonify(companyDao.findEmpById(empID))

#get all employees by department id route
# curl http://127.0.0.1:5000/employees/dept/1
@app.route('/employees/dept/<int:deptID>')
def getAllEmpByDept(deptID):
   return jsonify(companyDao.getAllEmpByDept(deptID))

# find By user id route
# curl http://127.0.0.1:5000/u/1
@app.route('/u/<int:userID>')
def findUserByID(userID):
   return jsonify(companyDao.findUserByID(userID))

# create department route
# curl -X POST -d "{\"name\":\"hr\", \"location\":\"dublin\", \"budget\":100000}" -H "Content-Type:application/json" http://127.0.0.1:5000/departments
# curl -X POST -d "{\"name\":\"sales\", \"location\":\"kilkenny\", \"budget\":250000}" -H "Content-Type:application/json" http://127.0.0.1:5000/departments
@app.route('/departments', methods=['POST'])
def createDept():
   if not request.json:
      abort(400)
   dept = {
      "name": request.json["name"],
      "location": request.json["location"],
      "budget": request.json["budget"]
   }
   return jsonify(companyDao.createDept(dept))

# create employee route
# curl -X POST -d "{\"name\":\"mary\", \"address\":\"dublin\", \"salary\":60100, \"dept\":1}" -H "Content-Type:application/json" http://127.0.0.1:5000/employees
# curl -X POST -d "{\"name\":\"tom\", \"address\":\"wicklow\", \"salary\":57000, \"dept\":1}" -H "Content-Type:application/json" http://127.0.0.1:5000/employees
# curl -X POST -d "{\"name\":\"sarah\", \"address\":\"carlow\", \"salary\":42000, \"dept\":2}" -H "Content-Type:application/json" http://127.0.0.1:5000/employees
@app.route('/employees', methods=['POST'])
def createEmp():
   if not request.json:
      abort(400)
   # check if dept exists
   dept = request.json["dept"]
   checkDept = companyDao.findDeptById(dept)
   if checkDept == {}:
      return jsonify({}), 404
   emp = {
      "name": request.json["name"],
      "address": request.json["address"],
      "salary": request.json["salary"],
      "dept": request.json["dept"]
   }
   return jsonify(companyDao.createEmp(emp))

# create user route
# curl -X POST -d "{\"name\":\"sarah\", \"password\":\"pass\"}" -H "Content-Type:application/json" http://127.0.0.1:5000/u
@app.route('/u', methods=['POST'])
def createUser():
   if not request.json:
      abort(400)
   u = {
      "name": request.json["name"],
      "password": request.json["password"]
   }
   return jsonify(companyDao.createUser(u))

#update department route
# curl -X PUT -d "{\"name\":\"it\", \"budget\":200000}" -H "content-type:application/json" http://127.0.0.1:5000/departments/2
@app.route('/departments/<int:deptID>', methods=['PUT'])
def updateDept(deptID):
   # foundDept = companyDao.findDeptById(deptID)
   # print(foundDept)
   if foundDept == {}:
      return jsonify({}), 404
   currentDept = foundDept
   if 'name' in request.json:
      currentDept['name'] = request.json['name']
   if 'location' in request.json:
      currentDept['location'] = request.json['location']
   if 'budget' in request.json:
      currentDept['budget'] = request.json['budget']
   companyDao.updateDept(currentDept)
   return jsonify(currentDept)

#update employee route
# curl -X PUT -d "{\"empID\": 3, \"name\": \"sean\", \"salary\": 30000, \"dept\": 1}" -H "content-type:application/json" http://127.0.0.1:5000/employees/2
@app.route('/employees/<int:empID>', methods=['PUT'])
def updateEmp(empID):
   foundEmp = companyDao.findEmpById(empID)
   # print(foundEmp)
   if foundEmp == {}:
      return jsonify({}), 404
   currentEmp = foundEmp
   if 'name' in request.json:
      currentEmp['name'] = request.json['name']
   if 'address' in request.json:
      currentEmp['address'] = request.json['address']
   if 'salary' in request.json:
      currentEmp['salary'] = request.json['salary']
   if 'dept' in request.json:
      # check if dept exists. deptID has to exist to assign an employee to a deptID
      deptID = request.json['dept']
      checkDept = companyDao.findDeptById(deptID)
      if checkDept == {}:
         return jsonify({}), 404
      currentEmp['dept'] = deptID
   companyDao.updateEmp(currentEmp)
   return jsonify(currentEmp)

#update user route
# curl -X PUT -d "{\"name\":\"mary\", \"password\":\"xyz\"}" -H "content-type:application/json" http://127.0.0.1:5000/u/2
@app.route('/u/<int:userID>', methods=['PUT'])
def updateUser(userID):
   foundUser = companyDao.findUserByID(userID)
   print(foundUser)
   if foundUser == {}:
      return jsonify({}), 404
   currentUser = foundUser
   if 'name' in request.json:
      currentUser['name'] = request.json['name']
   if 'password' in request.json:
      currentUser['password'] = request.json['password']
   companyDao.updateUser(currentUser)
   return jsonify(currentUser)

#delete department route
# curl -X DELETE http://127.0.0.1:5000/departments/1
@app.route('/departments/<int:deptID>', methods=['DELETE'])
def deleteDept(deptID):
   # check if dept exists
   foundDept = companyDao.findDeptById(deptID)
   if foundDept == {}:
      return jsonify({"done": False}), 404
   companyDao.deleteDept(deptID)
   return jsonify({"done": True})

#delete employee route
# curl -X DELETE http://127.0.0.1:5000/employees/1
@app.route('/employees/<int:empID>', methods=['DELETE'])
def deleteEmp(empID):
   # check if emp exists
   foundEmp = companyDao.findEmpById(empID)
   if foundEmp == {}:
      return jsonify({"done": False}), 404
   companyDao.deleteEmp(empID)
   return jsonify({"done": True})

#delete user route
# curl -X DELETE http://127.0.0.1:5000/u/2
@app.route('/u/<int:userID>', methods=['DELETE'])
def deleteUser(userID):
   # check if dept exists
   foundUser = companyDao.findUserByID(userID)
   if foundUser == {}:
      return jsonify({"done": False}), 404
   companyDao.deleteUser(userID)
   return jsonify({"done": True})

if __name__ == "__main__":
   # app.run(debug=True)
   app.run()
