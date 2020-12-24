# Data Representation Project 2020
**GMIT Lecturer:** Andrew Beatty
**Author:** Mark Cotter g00376335@gmit.ie
**Project:** Company Database

### Database Description Plan
A database 'company' is required to manage department and employee information and has two tables 'departments' and 'employees'. The database also has a third table 'users' to store database login access information.

The 'departments' table has the following data fields:
* deptID (PRIMARY KEY)
* name
* location
* budget

The 'employees' table has the following data fields and links to the 'departments' table using the foreign key 'dept' that is associated with the filed 'deptID' in the 'departments' table:
* empID (PRIMARY KEY)
* name
* address
* salary
* dept (FOREIGN KEY)

A company application user table 'users' is for storing database user login access information and has the following data fields:
* userID (PRIMARY KEY)
* name
* password

This database is stored in an sql database, which has an initialisation file 'initdb.sql'. The sql commands to create the database 'company' and its associated tables 'departments', 'employees' and 'users are stored in this initialisation file.

### Company sql Database Access Object (DAO)
The DAO for the 'company' database has been created in the class file 'CompanyDao.py', which creates an instance of the class called 'companyDao' that can be used in with an associated python server to undertake CRUD operations for the sql database. The sql database login configuration specific for each machine and user are stored in the 'dbconfig.py' file. A connection pool is used to make database connections.

### Flask Server
A python server called 'server.py' has been created using Python flask for undertaking database CRUD operations in association with the 'company' sql DAO. The server can be run from the command line by typing the command 'python server.py'. The server includes some basic session login checks and logging of the database CRUD operations.

### App Login
A basic login page 'login.html' is included in the 'templates' folder has been added to the front end of the app. The login page is accessible via the root address "/login" of the app (localhost 'http://127.0.0.1:5000/login') or as a redirect if accessing the database. The submitted login form does not have a secure authentication for the password. A more secure method of login authentication should be undertaken for a publication version of the app. Allowable "user : password" combinations are:
* admin : admin
* mark : 1234
* andrew : abcd

### App Index GUI page
A HTML user interface page 'Index.html' is included the 'templates' folder. This Graphical User Interface (GUI) can be used to view and undertake CRUD operations on the database content. Once the flask server is running, the GUI can be accessed from a web browser after logging in at the login page. The Index page is accessible once logged via the root address "/" of the app (localhost 'http://127.0.0.1:5000/').

### Virtual environment
Conda was used to create a localhost virtual environment (venv) for the server to run on using the following command line commands to create the venv, install and save packages for the venv, set the flask_app server and server mode, run the server, stop the server and finally deactivate the venv.

* λ conda create --name venv python=3.8
* λ conda activate venv
* (venv)λ pip install Flask
* (venv)λ pip install mysql-connector-python
* (venv)λ pip freeze > requirements.txt
* (venv)λ set FLASK_APP=server
* (venv)λ set FLASK_ENV=development
* (venv)λ flask run
* Crtl+c
* (venv)λ conda deactivate

The package requirements can also be install from the list in the file 'requirement.txt' using the venv command
* (venv)λ pip install -r requirements.txt

### Deployment to pythonanywhere.com
The database app has been deployed to pythonanywhere cloud at the address http://markcotter.pythonanywhere.com/. The app is running an Ubuntu virtual machine with minimal software modules listed in the 'requirement.txt' file. The SQL database for the deployed version of the app is also stored on the pythonanywhere cloud.