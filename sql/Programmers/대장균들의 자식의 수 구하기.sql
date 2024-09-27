SELECT A.ID,
IFNULL(
    (SELECT COUNT(DISTINCT ID)
    FROM ECOLI_DATA WHERE PARENT_ID = A.ID)
, 0) AS CHILD_COUNT
FROM ECOLI_DATA AS A
ORDER BY 1