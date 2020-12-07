from flask import Flask, url_for, request, redirect, abort, jsonify
from CompanyDao import companyDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')

# Root
# curl http://127.0.0.1:5000/
@app.route('/')
def index():
   return "hello"

#get all departments
# curl http://127.0.0.1:5000/departments
@app.route('/departments')
def getAllDept():
   return jsonify(companyDao.getAllDept())

#get all employees
# curl http://127.0.0.1:5000/employees
@app.route('/employees')
def getAllEmp():
   return jsonify(companyDao.getAllEmp())

# find By department id
# curl http://127.0.0.1:5000/departments/1
@app.route('/departments/<int:deptID>')
def findDeptById(deptID):
   return jsonify(companyDao.findDeptById(deptID))

# find By employee id
# curl http://127.0.0.1:5000/employees/1
@app.route('/employees/<int:empID>')
def findEmpById(empID):
   return jsonify(companyDao.findEmpById(empID))

#get all employees by department id
# curl http://127.0.0.1:5000/employees/hr
@app.route('/employees/<name>')
def getAllEmpByDept(name):
   return jsonify(companyDao.getAllEmpByDept(str(name)))

# create department
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

# create employee
# curl -X POST -d "{\"name\":\"mary\", \"address\":\"dublin\", \"salary\":60100, \"dept\":1}" -H "Content-Type:application/json" http://127.0.0.1:5000/employees
# curl -X POST -d "{\"name\":\"tom\", \"address\":\"wicklow\", \"salary\":57000, \"dept\":1}" -H "Content-Type:application/json" http://127.0.0.1:5000/employees
# curl -X POST -d "{\"name\":\"sarah\", \"address\":\"carlow\", \"salary\":42000, \"dept\":2}" -H "Content-Type:application/json" http://127.0.0.1:5000/employees
@app.route('/employees', methods=['POST'])
def createEmp():
   if not request.json:
      abort(400)
   emp = {
      "name": request.json["name"],
      "address": request.json["address"],
      "salary": request.json["salary"],
      "dept": request.json["dept"]
   }
   return jsonify(companyDao.createEmp(emp))

#update department
# curl -X PUT -d "{\"name\":\"it\", \"budget\":200000}" -H "content-type:application/json" http://127.0.0.1:5000/departments/2
@app.route('/departments/<int:deptID>', methods=['PUT'])
def updateDept(deptID):
   foundDept = companyDao.findDeptById(deptID)
   print(foundDept)
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

#update employee
# curl -X PUT -d "{\"name\":\"sue\", \"salary\":30000}" -H "content-type:application/json" http://127.0.0.1:5000/employees/2
@app.route('/employees/<int:empID>', methods=['PUT'])
def updateEmp(empID):
   foundEmp = companyDao.findEmpById(empID)
   print(foundEmp)
   if foundEmp == {}:
      return jsonify({}), 404
   currentEmp = foundEmp
   if 'name' in request.json:
      currentEmp['name'] = request.json['name']
   if 'address' in request.json:
      currentEmp['address'] = request.json['address']
   if 'budget' in request.json:
      currentEmp['budget'] = request.json['budget']
   if 'dept' in request.json:
      currentEmp['dept'] = request.json['dept']
   companyDao.updateEmp(currentEmp)
   return jsonify(currentEmp)

#delete department
# curl -X DELETE http://127.0.0.1:5000/departments/1
@app.route('/departments/<int:deptID>', methods=['DELETE'])
def deleteDept(deptID):
   companyDao.deleteDept(deptID)
   return jsonify({"done": True})

#delete employee
# curl -X DELETE http://127.0.0.1:5000/employees/1
@app.route('/employees/<int:empID>', methods=['DELETE'])
def deleteEmp(empID):
   companyDao.deleteEmp(empID)
   return jsonify({"done": True})

if __name__ == "__main__":
   app.run(debug=True)
