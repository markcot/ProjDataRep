# Data Representation Project 2020
- GMIT Lecturer: Andrew Beatty
- Author: Mark Cotter g00376335@gmit.ie
- Project: Company Database

### Database Description Plan
A database 'company' is required to manage department and employee information and has two tables 'departments' and 'employees'.

The 'departments' table has the following data fields:
* deptID (PRIMARY KEY)
* name
* location
* budget

The 'employees' table has the following data fields and links to the 'departments' table using the foreign key 'dept'/'deptID':
* empID (PRIMARY KEY)
* name
* address
* salary
* dept (FOREIGN KEY)

This database is stored in an sql database, which has an initialisation file 'initdb.sql'. The sql commands to create the database 'company' and its associated tables 'departments' and 'employees' are stored in this file.

### Company sql Database Access Object (DAO)
The DAO for the 'company' database has been created in the class file 'CompanyDao.py', which creates an instance of the class called 'companyDao' that can be used in with an associated python server to undertake CRUD operations for the sql database. The sql database login configuration specific for each machine and user are stored in the 'dbconfig.py' file.

### Flask server
A python server called 'server.py' has been created using Python flask for undertaking CRUD operations in association with the 'company' sql DAO.