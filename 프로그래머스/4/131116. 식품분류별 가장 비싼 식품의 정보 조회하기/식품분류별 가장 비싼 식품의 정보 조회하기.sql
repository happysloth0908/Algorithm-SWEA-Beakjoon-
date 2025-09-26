-- 코드를 입력하세요
    SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
    FROM (
        SELECT *
        from FOOD_PRODUCT
        WHERE CATEGORY = '과자'
        ORDER BY PRICE DESC
        LIMIT 1
    ) as a
    

union
    SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
    FROM (
        SELECT *
        from FOOD_PRODUCT
        WHERE CATEGORY = '국'
        ORDER BY PRICE DESC
        LIMIT 1
    )as b
    
    union
    SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
    FROM (
        SELECT *
        from FOOD_PRODUCT
        WHERE CATEGORY = '김치'
        ORDER BY PRICE DESC
        LIMIT 1
    )as c
    
        union
    SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
    FROM (
        SELECT *
        from FOOD_PRODUCT
        WHERE CATEGORY = '식용유'
        ORDER BY PRICE DESC
        LIMIT 1
    )as d
    
ORDER BY MAX_PRICE DESC