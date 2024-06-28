-- 2019년에 order한 buyer의 id, join_date, 2019년에 몇번 주문했는지
SELECT U.user_id as 'buyer_id', U.join_date, COUNT(order_id) as 'orders_in_2019'
FROM Users as U LEFT JOIN Orders as O
ON U.user_id = O.buyer_id AND O.order_date LIKE '2019%'
GROUP BY 1
