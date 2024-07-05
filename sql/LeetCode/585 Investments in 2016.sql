SELECT ROUND(SUM(tiv_2016) ,2) as tiv_2016 FROM Insurance as I
WHERE tiv_2015 IN (
    SELECT tiv_2015 FROM Insurance as Ins WHERE Ins.pid != I.pid
)
AND (lat, lon) NOT IN (
    SELECT lat, lon FROM Insurance as Ins WHERE Ins.pid != I.pid
)