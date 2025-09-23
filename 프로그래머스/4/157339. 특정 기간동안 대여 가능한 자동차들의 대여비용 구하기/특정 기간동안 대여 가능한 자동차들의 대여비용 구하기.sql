SELECT c.CAR_ID, c.CAR_TYPE, FLOOR(c.daily_fee * 30 * ((100 - p.discount_rate)/100)) AS FEE
FROM CAR_RENTAL_COMPANY_CAR c LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN p ON c.CAR_TYPE = p.CAR_TYPE
WHERE  c.CAR_TYPE in ('세단' , 'SUV') and duration_type = '30일 이상' and c.CAR_ID not in
(SELECT CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
WHERE start_date <= 20221130 AND end_date >= 20221101)
AND c.daily_fee * 30 * ((100 - p.discount_rate)/100) >= 500000 AND c.daily_fee * 30 * ((100 - p.discount_rate)/100) < 2000000
ORDER BY 3 DESC, 2 ASC, 1 DESC