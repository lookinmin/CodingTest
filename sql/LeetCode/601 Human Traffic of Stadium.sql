/* Write your PL/SQL query statement below */
SELECT  DISTINCT s1.id,
        TO_CHAR(s1.visit_date, 'YYYY-MM-DD') visit_date,
        s1.people
FROM    Stadium s1, Stadium s2, Stadium s3
WHERE   s1.people >= 100
AND     s2.people >= 100
AND     s3.people >= 100
AND (
    (s1.id = s2.id - 1 AND s1.id = s3.id - 2) OR
    (s1.id = s2.id + 1 AND s1.id = s3.id - 1) OR
    (s1.id = s2.id + 1 AND s1.id = s3.id + 2)
)
ORDER BY visit_date;

-- CAN YOU OPTIMIZE THIS QUERY?
WITH C1 AS (
    SELECT  id,
            visit_date,
            people,
            id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM    Stadium 
    WHERE   people >= 100
)
SELECT  id,
        TO_CHAR(visit_date, 'YYYY-MM-DD') visit_date,
        people
FROM    C1
WHERE   grp IN (
    SELECT  grp 
    FROM    C1
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
ORDER BY visit_date;

-- COMPARE TWO QUERIES
-- 첫 번째 쿼리는 SELF JOIN을 사용하여 연속된 3일을 찾습니다.
-- 장점: 직관적이고 이해하기 쉬움
-- 단점: 3개의 테이블을 조인하므로 성능이 좋지 않을 수 있음

-- 두 번째 쿼리는 ROW_NUMBER()와 GROUP BY를 활용한 방식입니다.
-- 장점: 테이블 스캔이 한 번만 발생하여 성능이 더 좋음
-- 단점: 윈도우 함수를 사용하여 로직이 복잡해 보일 수 있음

-- 결론: 대용량 데이터의 경우 두 번째 쿼리가 더 효율적입니다.
-- 소규모 데이터나 가독성이 중요한 경우 첫 번째 쿼리도 좋은 선택이 될 수 있습니다.


