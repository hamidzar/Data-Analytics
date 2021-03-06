
Employee Database-SQL: A Mystery in Two Parts

Submitted By: Hamid Zarringhalam

![sql](sql.png)

In this assignment I designed the tables to hold data in the CSVs, import the CSVs into a SQL database, and answer questions about the data. 

### Data Engineering:
This section is about creating the tables under the schema. The Schemal Sql file is under Data Engineering folder

[Data Engineering](https://github.com/hamidzar/Data-Analytics/tree/master/SQL-Challenge/EmployeeSQL/Data%20Engineering)


### Data Analysis:
This section is about the queries and analysis on the employee database at Pewlett Hackard Corporation from the 1980s and 1990s. The data of this period is stored in six CSV files under "Resources" folder.

[Resources](https://github.com/hamidzar/Data-Analytics/tree/master/SQL-Challenge/EmployeeSQL/Resources)

The Data Analysis sql file is stored under "Data Analysis" folder:

[Data Analysis](https://github.com/hamidzar/Data-Analytics/tree/master/SQL-Challenge/EmployeeSQL/Data%20Analysis)


In this project, tables were created with the relative filed in the CSV files, then imported the CSVs into a SQL database under the tables, and the data queries was conducted to answer the questions.

1-List the following details of each employee: employee number, last name, first name, sex, and salary.

![SQL-Query-01](https://github.com/hamidzar/Data-Analytics/blob/master/SQL-Challenge/EmployeeSQL/Images/SQL-Query-01.PNG)

2-List first name, last name, and hire date for employees who were hired in 1986.

![SQL-Query-02](https://github.com/hamidzar/Data-Analytics/blob/master/SQL-Challenge/EmployeeSQL/Images/SQL-Query-02.PNG)

3-List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.

![SQL-Query-03](https://github.com/hamidzar/Data-Analytics/blob/master/SQL-Challenge/EmployeeSQL/Images/SQL-Query-03.PNG)

4-List the department of each employee with the following information: employee number, last name, first name, and department name.

![SQL-Query-04](https://github.com/hamidzar/Data-Analytics/blob/master/SQL-Challenge/EmployeeSQL/Images/SQL-Query-04.PNG)

5-List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."

![SQL-Query-05](https://github.com/hamidzar/Data-Analytics/blob/master/SQL-Challenge/EmployeeSQL/Images/SQL-Query-05.PNG)

6-List all employees in the Sales department, including their employee number, last name, first name, and department name.

![SQL-Query-06](https://github.com/hamidzar/Data-Analytics/blob/master/SQL-Challenge/EmployeeSQL/Images/SQL-Query-06.PNG)

7-List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

![SQL-Query-07](https://github.com/hamidzar/Data-Analytics/blob/master/SQL-Challenge/EmployeeSQL/Images/SQL-Query-07.PNG)

8-In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

![SQL-Query-08](https://github.com/hamidzar/Data-Analytics/blob/master/SQL-Challenge/EmployeeSQL/Images/SQL-Query-08.PNG)



### Data Modeling:

To model the employee data, ERD data modeling technique calledwhich is called Entity-Relationship Diagrams (ERD) is used.
 By using this technique the relation of tables and KEYs are identified. 
 
 [Entity-Relationship Diagrams](https://github.com/hamidzar/Data-Analytics/tree/master/SQL-Challenge/EmployeeSQL/ERD-%20Entity%20Relationship%20Diagram)

### Bonus:

In this section, I imported the data to Pandas and created a histogram to visualize the most common salary ranges for employees and 

a bar chart of average salary by title.

[Pandas code](https://github.com/hamidzar/Data-Analytics/blob/master/SQL-Challenge/EmployeeSQL/EmployeeDB-Validation.ipynb)

[Output](https://github.com/hamidzar/Data-Analytics/tree/master/SQL-Challenge/EmployeeSQL/Images)

### Epilogue

You look down at your badge to see that your employee ID number is 499942.

![SQL-Query-09](https://github.com/hamidzar/Data-Analytics/blob/master/SQL-Challenge/EmployeeSQL/Images/SQL-Query-09.PNG)
