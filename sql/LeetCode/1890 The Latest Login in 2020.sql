# Write your MySQL query statement below
SELECT user_id, MAX(time_stamp) as last_stamp FROM Logins
WHERE YEAR(time_stamp) = '2020'
GROUP BY 1 