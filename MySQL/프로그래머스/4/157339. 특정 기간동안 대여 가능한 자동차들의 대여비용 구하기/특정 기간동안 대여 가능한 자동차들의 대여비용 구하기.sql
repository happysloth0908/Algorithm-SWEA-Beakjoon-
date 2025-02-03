-- 대여 가능한 차량을 찾기 위한 임시 테이블(CTE) 생성
WITH AVAILABLE_CARS AS (
   SELECT DISTINCT C.CAR_ID
   FROM CAR_RENTAL_COMPANY_CAR C
   WHERE C.CAR_TYPE IN ('세단', 'SUV')  -- 세단과 SUV만 필터링
   AND NOT EXISTS (  -- 대여 기간이 겹치지 않는 차량만 선택
       SELECT 1 
       FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
       WHERE C.CAR_ID = H.CAR_ID
       AND H.START_DATE <= '2022-11-30'  -- 대여 종료일이 11월 1일 이후이고
       AND H.END_DATE >= '2022-11-01'    -- 대여 시작일이 11월 30일 이전인 경우는 제외
   )
)

-- 메인 쿼리
SELECT 
   C.CAR_ID,
   C.CAR_TYPE,
   FLOOR(C.DAILY_FEE * (1 - D.DISCOUNT_RATE/100) * 30) AS FEE  -- 30일 대여 금액 계산
FROM 
   CAR_RENTAL_COMPANY_CAR C
   JOIN AVAILABLE_CARS A ON C.CAR_ID = A.CAR_ID  -- 대여 가능한 차량과 조인
   JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN D  -- 할인 정책 테이블과 조인
       ON C.CAR_TYPE = D.CAR_TYPE 
       AND D.DURATION_TYPE = '30일 이상'  -- 30일 이상 할인율 적용

-- 대여 금액이 50만원 이상 200만원 미만인 차량만 필터링
WHERE 
   C.DAILY_FEE * (1 - D.DISCOUNT_RATE/100) * 30 BETWEEN 500000 AND 1999999

-- 정렬 조건:
-- 1. 대여 금액 내림차순
-- 2. 자동차 종류 오름차순
-- 3. 자동차 ID 내림차순
ORDER BY 
   FEE DESC,
   C.CAR_TYPE ASC,
   C.CAR_ID DESC;