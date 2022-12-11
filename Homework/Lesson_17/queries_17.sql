select count(distinct JOB_ID) from employees;

select avg(SALARY) as SALARY_AVG, count(EMPLOYEE_ID) as EMPLOYEE_COUNT from employees where DEPARTMENT_ID = 90;

select JOB_ID, count(EMPLOYEE_ID) EMPLOYEE_COUNT from employees group by JOB_ID;

select FIRST_NAME, LAST_NAME, DEPARTMENT_ID from employees;

select e.FIRST_NAME, e.LAST_NAME, e.JOB_ID, e.DEPARTMENT_ID from
employees e join departments d on e.DEPARTMENT_ID = d.DEPARTMENT_ID
join locations l on d.LOCATION_ID = l.LOCATION_ID where l.CITY = 'London';