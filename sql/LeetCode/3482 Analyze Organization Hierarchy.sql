/* Write your PL/SQL query statement below */
select  employee_id,
        employee_name,
        level,
        (
            select  count(*)
            from    employees e2
            connect by prior employee_id = manager_id
            start with e2.manager_id = e1.employee_id
        ) as team_size,
        salary + nvl((
            select  sum(salary)
            from    employees e2
            connect by prior employee_id = manager_id
            start with e2.manager_id = e1.employee_id
        ), 0) as budget
from employees e1
start with manager_id is null
connect by prior employee_id = manager_id
order by level, budget desc, employee_name;