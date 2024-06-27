SELECT day, SUM(total_bill) as revenue_daily FROM tips
GROUP BY 1
HAVING SUM(total_bill) >= 1000
ORDER BY 2 DESC