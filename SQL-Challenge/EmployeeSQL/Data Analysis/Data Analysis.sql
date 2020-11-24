--Data Analysis
--1. List the following details of each employee: 
--employee number, last name, first name, sex, and salary.
SELECT a.emp_no,a.last_name, a.first_name,a.sex,b.salary 
FROM employees a 
JOIN salaries b
on a.emp_no = b.emp_no;

--2. List first name, last name, and hire date for employees who were hired in 1986.
Select first_name,last_name,hire_date 
FROM employees 
WHERE hire_date BETWEEN '1986-01-01' AND '1987-01-01'
ORDER BY hire_date;

--3. List the manager of each department with the following information:
--department number, department name, the manager's employee number, last name, first name.
SELECT a.dept_no, a.dept_name, b.emp_no, c.last_name, c.first_name
FROM departments a
JOIN dept_manager b
ON a.dept_no = b.dept_no
JOIN employees c
ON  b.emp_no= c.emp_no

--4. List the department of each employee with the following information:
--employee number, last name, first name, and department name.

--Created view to use for queries 6th & 7th
CREATE VIEW emp_dept_info AS 
SELECT a.emp_no, b.last_name, b.first_name, c.dept_name
FROM dept_emp a
JOIN employees b
ON a.emp_no = b.emp_no
JOIN departments c
ON a.dept_no = c.dept_no;
	
--5. List first name, last name, and sex for employees 
--whose first name is "Hercules" and last names begin with "B."
SELECT first_name,last_name, sex 
FROM employees 
WHERE first_name= 'Hercules' and last_name LIKE 'B%';

--6. List all employees in the Sales department,
--including their employee number, last name, first name, and department name.
SELECT emp_no, last_name, first_name, dept_name
FROM emp_dept_info
WHERE dept_name = 'Sales';

--7. List all employees in the Sales and Development departments,
--including their employee number, last name, first name, and department name.
SELECT emp_no, last_name, first_name, dept_name
FROM emp_dept_info
WHERE dept_name IN ('Sales', 'Development');

--8. In descending order, list the frequency count of employee last names,
--i.e., how many employees share each last name.
Select last_name,count(last_name) as "frequency"
FROM employees
GROUP BY last_name 
ORDER BY frequency DESC ;

--Epilogue: "Search your ID number." You look down at your badge to see that your employee ID number is 499942
SELECT last_name as "Last Name", first_name as "First Name"
FROM employees
WHERE emp_no = '499942';