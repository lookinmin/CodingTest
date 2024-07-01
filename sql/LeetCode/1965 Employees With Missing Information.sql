# Write your MySQL query statement below
SELECT e.employee_id FROM Employees as e
LEFT JOIN Salaries as s USING(employee_id)
WHERE salary IS NULL

UNION

SELECT s.employee_id FROM Employees as e
RIGHT JOIN Salaries as s USING(employee_id)
WHERE name IS NULL

ORDER BY employee_id;