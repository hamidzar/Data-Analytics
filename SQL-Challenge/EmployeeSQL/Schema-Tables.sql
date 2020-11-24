-- Data Engineering
DROP TABLE IF EXISTS departments CASCADE;
DROP TABLE IF EXISTS titles CASCADE;
DROP TABLE IF EXISTS employees CASCADE;
DROP TABLE IF EXISTS dept_emp CASCADE;
DROP TABLE IF EXISTS dept_manager CASCADE;
DROP TABLE IF EXISTS salaries CASCADE;

CREATE TABLE "departments" (
    "dept_no" VARCHAR(8) PRIMARY KEY NOT NULL,
    "dept_name" VARCHAR(40) NOT NULL
);

CREATE TABLE "titles" (
    "title_id" VARCHAR(8) PRIMARY KEY NOT NULL,
    "title" VARCHAR(30) NOT NULL
);

CREATE TABLE "employees" (
    "emp_no" INT PRIMARY KEY NOT NULL,
    "emp_title_id" VARCHAR(8) NOT NULL,
	foreign key (emp_title_id) references titles(title_id),
    "birth_date" DATE NOT NULL,
    "first_name" VARCHAR(20) NOT NULL,
    "last_name" VARCHAR(20) NOT NULL,
    "sex" VARCHAR(2) NOT NULL,
    "hire_date" DATE  NOT NULL
);

CREATE TABLE "dept_emp" (
    "emp_no" INT NOT NULL,
	foreign key (emp_no) references employees(emp_no),
    "dept_no" VARCHAR(10)   NOT NULL,
	foreign key (dept_no) references departments (dept_no)
);

CREATE TABLE "dept_manager" (
    "dept_no" VARCHAR(8) NOT NULL,
	foreign key (dept_no) references departments (dept_no),
    "emp_no" INT NOT NULL,
	foreign key (emp_no) references employees(emp_no)
);

CREATE TABLE "salaries" (
    "emp_no" INT   NOT NULL,
	foreign key (emp_no) references employees(emp_no),
    "salary" INT NOT NULL
);
-- Viewing the tables 
SELECT * FROM departments;
SELECT * FROM titles;	
SELECT * FROM employees;	
SELECT * FROM dept_emp;
SELECT * FROM dept_manager;	
SELECT * FROM salaries;