# left join
select * from employees left join jobs on employees.JOB_ID = jobs.JOB_ID;

# right join
select * from employees right join jobs on employees.JOB_ID = jobs.JOB_ID;

# full join
select * from employees full join jobs;

# cross join
select * from employees cross join jobs