SELECT S.user_id,
ROUND(AVG(IF(C.action = 'confirmed', 1, 0)), 2) as confirmation_rate
FROM Signups as S LEFT JOIN Confirmations as C
ON S.user_id = C.user_id
GROUP BY 1