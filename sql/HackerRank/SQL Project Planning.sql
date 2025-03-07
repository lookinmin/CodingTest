SELECT MIN(START_DATE), MAX(END_DATE) FROM
(
    SELECT START_DATE, END_DATE,
    START_DATE - ROW_NUMBER() OVER(ORDER BY START_DATE) AS RNK
    FROM PROJECTS
) AS SUB
GROUP BY RNK
ORDER BY DATEDIFF(MAX(END_DATE), MIN(START_DATE)), MIN(START_DATE);