CREATE DATABASE company;

USE company;

CREATE TABLE departments(
	deptID INT NOT NULL AUTO_INCREMENT,
   name VARCHAR(255) DEFAULT NULL,
   location varchar(255) DEFAULT NULL,
   budget INT DEFAULT NULL,
   PRIMARY KEY (deptID)
   );    

CREATE TABLE employees(
	empID INT NOT NULL AUTO_INCREMENT,
   name VARCHAR(255) DEFAULT NULL,
   address VARCHAR(255) DEFAULT NULL,
   salary INT DEFAULT NULL,
   dept INT DEFAULT NULL,
   PRIMARY KEY (empID),
   CONSTRAINT FK_deptEmp
   FOREIGN KEY (dept)
   REFERENCES departments(deptID)
      ON DELETE RESTRICT
   );

CREATE TABLE users(
	userID INT NOT NULL AUTO_INCREMENT,
   name VARCHAR(255) DEFAULT NULL,
   password varchar(255) DEFAULT NULL,
   PRIMARY KEY (userID)
   );

INSERT INTO departments (name, location, budget) VALUES ("hr", "dublin", 100000);
INSERT INTO departments (name, location, budget) VALUES ("sales", "kilkenny", 250000);
INSERT INTO departments (name, location, budget) VALUES ("it", "meath", 70000);
INSERT INTO employees (name, address, salary, dept) VALUES ("mary", "dublin", 60100, 1);
INSERT INTO employees (name, address, salary, dept) VALUES ("tom", "wicklow", 57000, 2);
INSERT INTO employees (name, address, salary, dept) VALUES ("sarah", "carlow", 42000, 2);
INSERT INTO employees (name, address, salary, dept) VALUES ("simon", "galway", 45000, 3);

INSERT INTO users (name, password) VALUES ("admin", "admin");
INSERT INTO users (name, password) VALUES ("mark", "1234");
INSERT INTO users (name, password) VALUES ("andrew", "abcd");