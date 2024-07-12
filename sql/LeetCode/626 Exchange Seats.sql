SELECT IF(id < (SELECT MAX(id) FROM Seat), 
IF(MOD(id, 2) = 0, id - 1, id + 1), 
IF(MOD(id, 2) = 0, id - 1, id)) as id, student
FROM Seat
ORDER BY 1