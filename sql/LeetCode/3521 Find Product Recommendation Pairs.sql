-- 1. 동일 고객이 구매한 상품 쌍(product1 < product2)을 찾고,
--    각 쌍을 구매한 고유 고객 수를 세어 최소 3명 이상인 쌍만 선택
WITH FrequentPairs AS (    
    SELECT
        pp1.product_id AS product1_id,
        pp2.product_id AS product2_id,
        COUNT(DISTINCT pp1.user_id) AS customer_count -- 고유 고객 수 계산
    FROM
        ProductPurchases pp1,
        ProductPurchases pp2
    WHERE   1=1
    AND     pp1.user_id = pp2.user_id   -- 같은 고객
    AND     pp1.product_id < pp2.product_id     -- 상품 쌍 조건
    GROUP BY
        pp1.product_id,
        pp2.product_id
    HAVING
        COUNT(DISTINCT pp1.user_id) >= 3 -- 최소 3명 조건
)
-- 2. 위에서 찾은 쌍에 상품 카테고리 정보를 조인하고 최종 정렬
SELECT
    fp.product1_id,
    fp.product2_id,
    pi1.category AS product1_category,
    pi2.category AS product2_category,
    fp.customer_count
FROM
    FrequentPairs fp,
    ProductInfo pi1,
    ProductInfo pi2
WHERE   1=1
AND     fp.product1_id = pi1.product_id -- 상품1 카테고리
AND     fp.product2_id = pi2.product_id -- 상품2 카테고리
ORDER BY
    fp.customer_count DESC, -- 고객 수 내림차순
    fp.product1_id,     -- 상품1 ID 오름차순
    fp.product2_id      -- 상품2 ID 오름차순