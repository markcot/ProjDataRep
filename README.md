# Data Representation Project 2020
**GMIT Lecturer:** Andrew Beatty
**Author:** Mark Cotter g00376335@gmit.ie
**Project:** Company Database

### Database Description
A database 'company' is required to manage department and employee information in two tables 'departments' and 'employees'. The database also has a third table 'users' to store database login access information.

The 'departments' table has the following data fields:
* deptID (PRIMARY KEY)
* name
* location
* budget

The 'employees' table has the following data fields and links to the 'departments' table using the foreign key 'dept' that is associated with the field 'deptID' in the 'departments' table:
* empID (PRIMARY KEY)
* name
* address
* salary
* dept (FOREIGN KEY)

The 'users' table is for storing database user login access information and has the following data fields:
* userID (PRIMARY KEY)
* name
* password

Sql was used to implemented the database. The sql commands to create the database 'company', its associated tables 'departments', 'employees' and 'users and populate the initial database content are stored in the initialisation file 'initdb.sql'.

### Company sql Database Access Object (DAO)
A DAO for the 'company' database has been created in the class file 'CompanyDao.py', which creates an instance of the class called 'companyDao' that is used with an associated python server to undertake user login and CRUD operations on the sql database. The sql database login configuration specific for each machine and user are stored in the 'dbconfig.py' file. A template version of this file 'dbconfigtemplate.py' is included in this repository. This template has to edited to match the specific requirements for each machine the database is running on and saved locally as 'dbconfig.py' for the DAO to read it. A connection pool is used to make database connections.

### Flask Server
A server app called 'server.py' has been created using Python flask for dealing with requests and responses for user login and database CRUD operations in association with the 'company' sql DAO. The server includes some basic session login checks and logging of the database CRUD operations. The server can be run locally from the command line by typing the command 'python server.py' or via a local or remote virtual environment.

### GUI App Interface
A graphical user interface app for the company database was designed in HTML for use on the Google Chrome browser. The interface page use the latest Bootstrap CSS sheet styles from https://getbootstrap.com/ and AJAX/jQuery library from https://developers.google.com/speed/libraries. The HTML interface includes a login and a index page that use flask templates for login authentication and routing.

#### GUI App Login page
A basic login page 'login.html' is included in the 'templates' folder of this repository. The login page is accessible via the server url route "host_url/login" or if using a localhost 'http://127.0.0.1:5000/login'. If not logged on some of the other server url routes also redirect to the login page. The submitted login form does not have a secure authentication for the password. Chrome gives a pop up warning in relation to the password not being secured, but this can be ignored. A more secure method of password login authentication should be undertaken for a more secure version of the app. Allowable "user : password" combinations are:
* admin : admin
* mark : 1234
* andrew : abcd

#### GUI App Index page
A database graphical user interface page 'Index.html' is included the 'templates' folder of this repository. This interface can be used to view and undertake CRUD operations on the database content and logout from the interface. Once the app server is running, the interface Index page can be accessed from a web browser after logging in at the login page via the root url address "host_url/" or if using a localhost 'http://127.0.0.1:5000/'.

### Virtual environment
Conda was used to create a localhost virtual environment (venv) for running the server. The following Windowss command line python commands can be to create the venv, install and save packages for the venv, set the flask_app server and server mode, run the server, stop the server and finally deactivate the venv.

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
The database app has been deployed to the pythonanywhere cloud server at the address:

* http://markcotter.pythonanywhere.com/

The deployed app interface runs on an Ubuntu virtual machine with the minimal software modules listed in the 'requirement.txt' file. The SQL database for the deployed app is also stored on the pythonanywhere cloud server.