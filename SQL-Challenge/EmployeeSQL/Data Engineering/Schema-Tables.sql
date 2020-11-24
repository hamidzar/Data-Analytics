-- Data Engineering

--DROP TABLE salary
DROP TABLE IF EXISTS departments CASCADE;
DROP TABLE IF EXISTS titles CASCADE;
DROP TABLE IF EXISTS employees CASCADE;
DROP TABLE IF EXISTS dept_emp CASCADE;
DROP TABLE IF EXISTS dept_manager CASCADE;
DROP TABLE IF EXISTS salaries CASCADE;

-- Create tables and insert values

CREATE TABLE employees (
 	emp_no INT NOT NULL,
	PRIMARY KEY (emp_no),
	emp_title_id VARCHAR NOT NULL,
	FOREIGN KEY (emp_title_id) REFERENCES titles (title_id),
	birth_date DATE NOT NULL,
  	first_name VARCHAR NOT NULL,
	last_name VARCHAR NOT NULL,
	sex VARCHAR NOT NULL,
	hire_date DATE NOT NULL
);

CREATE TABLE titles (
	title_id VARCHAR NOT NULL,
	PRIMARY KEY (title_id),
	title VARCHAR NOT NULL
);

CREATE TABLE salaries (
	emp_no INT NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees (emp_no),
	salary INT NOT NULL
);

CREATE TABLE departments (
	dept_no VARCHAR NOT NULL,
	PRIMARY KEY (dept_no),
	dept_name VARCHAR NOT NULL
);

CREATE TABLE dept_manager (
	dept_no VARCHAR NOT NULL,
	FOREIGN KEY (dept_no) REFERENCES departments(dept_no),
	emp_no INT NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no)
);

CREATE TABLE dept_emp (
	emp_no INT NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_no),
	dept_no VARCHAR NOT NULL,
	FOREIGN KEY (dept_no) REFERENCES departments(dept_no)
);

-- Viewing the tables 
SELECT * FROM departments;
SELECT * FROM titles;	
SELECT * FROM employees;	
SELECT * FROM dept_emp;
SELECT * FROM dept_manager;	
SELECT * FROM salaries;