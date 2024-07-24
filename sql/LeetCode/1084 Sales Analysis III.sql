# Write your MySQL query statement below
SELECT S.product_id, P.product_name FROM Product as P JOIN Sales as S
ON P.product_id = S.product_id
WHERE S.sale_date BETWEEN '2019-01-01' AND '2019-03-31'
AND S.product_id NOT IN (SELECT product_id FROM Sales WHERE sale_date > '2019-03-31' OR sale_date < '2019-01-01')
GROUP BY 1, 2