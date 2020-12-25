# Flask app server to deal with requests and responses between browser HTML Graphical User Interface
# and the Company Database Access Object (DAO) for user login and database CRUD operations

# import modules and DAO
from flask import Flask, url_for, request, redirect, abort, jsonify, session, abort, render_template
from CompanyDao import companyDao
# from logging.config import dictConfig

# # Logger config. Code verbatim from https://flask.palletsprojects.com/en/1.1.x/logging/
# # ========================== NOT USED ===============================
# # Does not work with the pythonanywhere cloud server 
#
# dictConfig({
#    'version': 1,
#    'formatters': {'default': {
#       'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
#    }},
#    'handlers': {'wsgi': {
#       'class': 'logging.StreamHandler',
#       'stream': 'ext://flask.logging.wsgi_errors_stream',
#       'formatter': 'default'
#    }},
#    'root': {
#       'level': 'INFO',
#       'handlers': ['wsgi']
#    }
# })
# # ==================================================================

# Define flask app and session secret key
app = Flask(__name__)
app.secret_key = 'akuye5edFVNcn5eceCECnlnyax6Dcsc'

# Root route - Link to Index
# curl http://127.0.0.1:5000/
@app.route('/')
def index():
   if not 'username' in session:
      return redirect(url_for('login'))

   return render_template('index.html', title='Index', name = session['username'])

# Login route
# Code adapted from https://pythonbasics.org/flask-http-methods/
# curl http://127.0.0.1:5000/login
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      submittedName = request.form['name']
      submittedPassword = request.form['password']

      # Get users from database
      foundUsers = companyDao.getAllUser()
      for i in range(len(foundUsers)):
         # compare user name
         if submittedName.lower() == foundUsers[i]["name"].lower():
            app.logger.info('User found')
            # compare user password
            if submittedPassword == foundUsers[i]["password"]:
               # username and associated password match found
               app.logger.info('Password matched for user %s', submittedName)
               session['username'] = submittedName
               return redirect(url_for('index',name = session['username']))
            else:
               app.logger.info('Password does not match for user')
               return render_template('login.html', title='Login', userMessage='WARNING: Incorrect password entered! Please try again')
         
      # Otherwise               
      app.logger.info('User not found')
      return render_template('login.html', title='Login', userMessage='WARNING: User not found! Please try again')

   else:
      # for GET method
      app.logger.info('Redirect to login')
      return render_template('login.html', title='Login', userMessage='Please Login')

# Logout route
# curl http://127.0.0.1:5000/logout
@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('login'))

# get all departments route
# curl http://127.0.0.1:5000/departments
@app.route('/departments')
def getAllDept():
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   app.logger.info('Get all deparments')
   return jsonify(companyDao.getAllDept())

# get all employees route
# curl http://127.0.0.1:5000/employees
@app.route('/employees')
def getAllEmp():
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   app.logger.info('Get all employees')
   return jsonify(companyDao.getAllEmp())

# get all users route
# curl http://127.0.0.1:5000/u
@app.route('/u')
def getAllUser():
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   app.logger.info('Get all users')
   return jsonify(companyDao.getAllUser())

# find By department id route
# curl http://127.0.0.1:5000/departments/1
@app.route('/departments/<int:deptID>')
def findDeptById(deptID):
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   app.logger.info('Get dept with deptID %s', deptID)
   return jsonify(companyDao.findDeptById(deptID))

# find By employee id route
# curl http://127.0.0.1:5000/employees/1
@app.route('/employees/<int:empID>')
def findEmpById(empID):
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   app.logger.info('Get emp with empID %s', empID)
   return jsonify(companyDao.findEmpById(empID))

# get all employees by department id route
# curl http://127.0.0.1:5000/employees/dept/1
@app.route('/employees/dept/<int:deptID>')
def getAllEmpByDept(deptID):
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   app.logger.info('Get all employees in dept with deptID %s', deptID)
   return jsonify(companyDao.getAllEmpByDept(deptID))

# find By user id route
# curl http://127.0.0.1:5000/u/1
@app.route('/u/<int:userID>')
def findUserByID(userID):
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   app.logger.info('Get user %s', userID)
   return jsonify(companyDao.findUserByID(userID))

# create department route, returns created dept info
# curl -X POST -d "{\"name\":\"hr\", \"location\":\"dublin\", \"budget\":100000}" -H "Content-Type:application/json" http://127.0.0.1:5000/departments
# curl -X POST -d "{\"name\":\"sales\", \"location\":\"kilkenny\", \"budget\":250000}" -H "Content-Type:application/json" http://127.0.0.1:5000/departments
@app.route('/departments', methods=['POST'])
def createDept():
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   if not request.json:
      app.logger.info('Request format not json')
      abort(400)
   dept = {
      "name": request.json["name"],
      "location": request.json["location"],
      "budget": request.json["budget"]
   }
   app.logger.info('Created dept %s', dept)
   return jsonify(companyDao.createDept(dept))

# create employee route, returns created emp info
# curl -X POST -d "{\"name\":\"mary\", \"address\":\"dublin\", \"salary\":60100, \"dept\":1}" -H "Content-Type:application/json" http://127.0.0.1:5000/employees
# curl -X POST -d "{\"name\":\"tom\", \"address\":\"wicklow\", \"salary\":57000, \"dept\":1}" -H "Content-Type:application/json" http://127.0.0.1:5000/employees
# curl -X POST -d "{\"name\":\"sarah\", \"address\":\"carlow\", \"salary\":42000, \"dept\":2}" -H "Content-Type:application/json" http://127.0.0.1:5000/employees
@app.route('/employees', methods=['POST'])
def createEmp():
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   if not request.json:
      app.logger.info('Request format not json')
      abort(400)
   # check if dept exists
   dept = request.json["dept"]
   checkDept = companyDao.findDeptById(dept)
   if checkDept == {}:
      app.logger.info('DeptID %s not found', checkDept.deptID)
      return jsonify({}), 404
   emp = {
      "name": request.json["name"],
      "address": request.json["address"],
      "salary": request.json["salary"],
      "dept": request.json["dept"]
   }
   app.logger.info('Created emp %s', emp)
   return jsonify(companyDao.createEmp(emp))

# create user route, returns created user info
# curl -X POST -d "{\"name\":\"sarah\", \"password\":\"pass\"}" -H "Content-Type:application/json" http://127.0.0.1:5000/u
@app.route('/u', methods=['POST'])
def createUser():
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   if not request.json:
      app.logger.info('Request format not json')
      abort(400)
   u = {
      "name": request.json["name"],
      "password": request.json["password"]
   }
   app.logger.info('Created user %s', user)
   return jsonify(companyDao.createUser(u))

# update department route, returns updated dept info
# curl -X PUT -d "{\"name\":\"it\", \"budget\":200000}" -H "content-type:application/json" http://127.0.0.1:5000/departments/2
@app.route('/departments/<int:deptID>', methods=['PUT'])
def updateDept(deptID):
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   if not request.json:
      app.logger.info('Request format not json')
      abort(400)
   foundDept = companyDao.findDeptById(deptID)
   # print(foundDept)
   if foundDept == {}:
      app.logger.info('DeptID %s not found', deptID)
      return jsonify({}), 404
   currentDept = foundDept
   if 'name' in request.json:
      currentDept['name'] = request.json['name']
   if 'location' in request.json:
      currentDept['location'] = request.json['location']
   if 'budget' in request.json:
      currentDept['budget'] = request.json['budget']
   companyDao.updateDept(currentDept)
   app.logger.info('Updated dept %s', currentDept)
   return jsonify(currentDept)

# update employee route, returns updated emp info
# curl -X PUT -d "{\"empID\": 3, \"name\": \"sean\", \"salary\": 30000, \"dept\": 1}" -H "content-type:application/json" http://127.0.0.1:5000/employees/2
@app.route('/employees/<int:empID>', methods=['PUT'])
def updateEmp(empID):
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   if not request.json:
      app.logger.info('Request format not json')
      abort(400)
   foundEmp = companyDao.findEmpById(empID)
   # print(foundEmp)
   if foundEmp == {}:
      app.logger.info('EmpID %s not found', empID)
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
         app.logger.info('DeptID %s not found', deptID)
         return jsonify({}), 404
      currentEmp['dept'] = deptID
   companyDao.updateEmp(currentEmp)
   app.logger.info('Updated emp %s', currentEmp)
   return jsonify(currentEmp)

#update user route, returns updated user info
# curl -X PUT -d "{\"name\":\"mary\", \"password\":\"xyz\"}" -H "content-type:application/json" http://127.0.0.1:5000/u/2
@app.route('/u/<int:userID>', methods=['PUT'])
def updateUser(userID):
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   if not request.json:
      app.logger.info('Request format not json')
      abort(400)
   foundUser = companyDao.findUserByID(userID)
   print(foundUser)
   if foundUser == {}:
      app.logger.info('UserID %s not found', userID)
      return jsonify({}), 404
   currentUser = foundUser
   if 'name' in request.json:
      currentUser['name'] = request.json['name']
   if 'password' in request.json:
      currentUser['password'] = request.json['password']
   companyDao.updateUser(currentUser)
   app.logger.info('Updated user %s', currentUser)
   return jsonify(currentUser)

# delete department route, returns True/False if delete was done
# curl -X DELETE http://127.0.0.1:5000/departments/1
@app.route('/departments/<int:deptID>', methods=['DELETE'])
def deleteDept(deptID):
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   # check if dept exists
   foundDept = companyDao.findDeptById(deptID)
   if foundDept == {}:
      app.logger.info('DeptID %s not found', deptID)
      return jsonify({"done": False}), 404
   try:
      companyDao.deleteDept(deptID)
      app.logger.info('Deleted dept %s', foundDept)
      return jsonify({"done": True})
   except:
      app.logger.info('Cannot delete deptID %s', deptID)
      return jsonify({"done": False})

# delete employee route, returns True/False if delete was done
# curl -X DELETE http://127.0.0.1:5000/employees/1
@app.route('/employees/<int:empID>', methods=['DELETE'])
def deleteEmp(empID):
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   # check if emp exists
   foundEmp = companyDao.findEmpById(empID)
   if foundEmp == {}:
      app.logger.info('EmpID %s not found', empID)
      return jsonify({"done": False}), 404
   companyDao.deleteEmp(empID)
   app.logger.info('Deleted emp %s', foundEmp)
   return jsonify({"done": True})

# delete user route, returns True/False if delete was done
# curl -X DELETE http://127.0.0.1:5000/u/2
@app.route('/u/<int:userID>', methods=['DELETE'])
def deleteUser(userID):
   if not 'username' in session:
      app.logger.info('Access not authorised')
      abort(401)
   # check if dept exists
   foundUser = companyDao.findUserByID(userID)
   if foundUser == {}:
      app.logger.info('UserID %s not found', userID)
      return jsonify({"done": False}), 404
   companyDao.deleteUser(userID)
   app.logger.info('Deleted user %s', foundUser)
   return jsonify({"done": True})

# initialise server app
if __name__ == "__main__":
   # app.run(debug=True)
   app.run()