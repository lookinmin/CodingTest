SELECT B.CATEGORY,
SUM(S.SALES) AS TOTAL_SALES
FROM BOOK AS B JOIN BOOK_SALES AS S USING(BOOK_ID)
WHERE S.SALES_DATE LIKE '2022-01%'
GROUP BY B.CATEGORY
ORDER BY 1