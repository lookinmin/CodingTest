SELECT YEAR(S.SALES_DATE) AS YEAR, MONTH(S.SALES_DATE) AS MONTH,
U.GENDER, COUNT(DISTINCT U.USER_ID) AS USERS
FROM USER_INFO AS U JOIN ONLINE_SALE AS S USING(USER_ID)
WHERE U.GENDER IS NOT NULL
GROUP BY YEAR(S.SALES_DATE), MONTH(S.SALES_DATE), U.GENDER
ORDER BY 1, 2, 3