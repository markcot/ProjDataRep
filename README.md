# Data Representation Project 2020
GMIT Lecturer: Andrew Beatty
Author: Mark Cotter g00376335@gmit.ie
Project: Company Database

### Database Description Plan
A database 'company' is required to manage department and employee information and has two tables 'departments' and 'employees'.
The 'departments' table has data fields
* deptID (PRIMARY KEY)
* name
* location
* budget

The 'employees' table has data fields and linked to the department table for the foreign key deptID
* empID (PRIMARY KEY)
* name
* address
* salary
* dept (FOREIGN KEY)