# functions
select avg(SALARY) from employees;
select count(*) from employees;
select count(distinct JOB_ID) from employees;
select count(distinct FIRST_NAME) from employees;
select min(SALARY) from employees;
select max(SALARY) from employees;
select sum(SALARY) from employees;
select round(SALARY, 1) from employees;
select first(SALARY) from employees;
select last(SALARY) from employees;
select ucase(FIRST_NAME) from employees;
select lcase(FIRST_NAME) from employees;
select mid(FIRST_NAME, 1, 20) from employees;
select mid(FIRST_NAME, 1, 5), now() as CorTime from employees;
select count(distinct mid(FIRST_NAME, 1, 5)), now() as CorTime from employees;
select length(FIRST_NAME) from employees;