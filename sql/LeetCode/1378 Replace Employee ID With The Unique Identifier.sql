SELECT U.unique_id, E.name FROM Employees as E
LEFT JOIN EmployeeUNI as U ON E.id = U.id