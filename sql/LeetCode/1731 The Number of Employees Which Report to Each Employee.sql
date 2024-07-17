# Write your MySQL query statement below
SELECT A.employee_id, A.name,
COUNT(B.employee_id) as reports_count,
ROUND(AVG(B.age), 0) as average_age
FROM Employees as A JOIN Employees as B ON A.employee_id = B.reports_to
GROUP BY 1, 2
ORDER BY 1

---------------------------------------

SELECT A.employee_id, A.name,
(SELECT COUNT(employee_id) FROM Employees WHERE reports_to = A.employee_id) as reports_count,
(SELECT ROUND(AVG(age), 0) FROM Employees WHERE reports_to = A.employee_id) as average_age
FROM Employees as A
HAVING reports_count > 0 AND average_age IS NOT NULL
ORDER BY employee_id