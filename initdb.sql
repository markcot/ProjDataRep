CREATE DATABASE company;

USE company;

CREATE TABLE department(
	deptID INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) DEFAULT NULL,
    location varchar(255) DEFAULT NULL,
    budget INT DEFAULT NULL,
    PRIMARY KEY (deptID)
    );    

CREATE TABLE employee(
	empID INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) DEFAULT NULL,
    address VARCHAR(255) DEFAULT NULL,
    salary INT DEFAULT NULL,
    dept INT DEFAULT NULL,
    PRIMARY KEY (empID),
    CONSTRAINT FK_deptEmp
		FOREIGN KEY (dept)
		REFERENCES department(deptID)
        ON DELETE SET NULL
    );