(SELECT CITY, LENGTH(CITY) FROM STATION
 ORDER BY 2, 1
 LIMIT 1)

UNION ALL

(SELECT CITY, LENGTH(CITY) FROM STATION
 ORDER BY 2 DESC, 1
 LIMIT 1)