/* Write your PL/SQL query statement below */
-- 1단계: 계절별, 카테고리별 판매 데이터 집계 (CTE 사용)
WITH SeasonalCategoryData AS (
    SELECT
        CASE
            WHEN TO_CHAR(a.sale_date, 'MM') IN ('12', '01', '02') THEN 'Winter'
            WHEN TO_CHAR(a.sale_date, 'MM') IN ('03', '04', '05') THEN 'Spring'
            WHEN TO_CHAR(a.sale_date, 'MM') IN ('06', '07', '08') THEN 'Summer'
            ELSE 'Fall' -- '09', '10', '11' 월에 해당
        END AS season,
        b.category,
        SUM(a.quantity) AS total_quantity,
        SUM(a.quantity * a.price) AS total_revenue
    FROM
        sales a,
        products b
    where   1=1
    and     a.product_id = b.product_id
    GROUP BY
        CASE
            WHEN TO_CHAR(a.sale_date, 'MM') IN ('12', '01', '02') THEN 'Winter'
            WHEN TO_CHAR(a.sale_date, 'MM') IN ('03', '04', '05') THEN 'Spring'
            WHEN TO_CHAR(a.sale_date, 'MM') IN ('06', '07', '08') THEN 'Summer'
            ELSE 'Fall'
        END,
        b.category
)
-- 2단계: 순위 매기기 및 최상위 카테고리 필터링 (FROM 절에 인라인 뷰(서브쿼리) 사용)
SELECT
    season,                                
    category,                              
    total_quantity, 
    total_revenue                         
FROM (
    SELECT
        season,
        category,
        total_quantity,
        total_revenue,
        ROW_NUMBER() OVER (
            PARTITION BY season             
            ORDER BY total_quantity DESC, 
                     total_revenue DESC         
        ) as rn
    FROM
        SeasonalCategoryData
) RankedData
WHERE
    rn = 1 -- 각 계절별 1위 카테고리만 선택
ORDER BY 1;