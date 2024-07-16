# Write your MySQL query statement below
SELECT A.employee_id, A.name,
COUNT(B.employee_id) as reports_count,
ROUND(AVG(B.age), 0) as average_age
FROM Employees as A JOIN Employees as B ON A.employee_id = B.reports_to
GROUP BY 1, 2
ORDER BY 1