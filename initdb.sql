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