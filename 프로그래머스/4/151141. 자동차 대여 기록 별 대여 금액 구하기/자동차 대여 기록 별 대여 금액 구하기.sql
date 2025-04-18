-- 코드를 입력하세요
WITH T1 AS (
    SELECT H.HISTORY_ID,
    H.CAR_ID, 
    C.DAILY_FEE*(DATEDIFF(H.END_DATE,H.START_DATE)+1) AS FEE,
    CASE
    WHEN DATEDIFF(H.END_DATE,H.START_DATE)+1 >= 90 THEN "90일 이상"
    WHEN DATEDIFF(H.END_DATE,H.START_DATE)+1 >= 30 THEN "30일 이상"
    WHEN DATEDIFF(H.END_DATE,H.START_DATE)+1 >= 7 THEN "7일 이상"
    ELSE "없음" END AS DURATION_TYPE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
    LEFT JOIN CAR_RENTAL_COMPANY_CAR C
    ON H.CAR_ID = C.CAR_ID
    WHERE C.CAR_TYPE = '트럭'),
    
    T2 AS (
    SELECT * FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    WHERE CAR_TYPE = "트럭")

SELECT T1.HISTORY_ID,
CASE 
WHEN T1.DURATION_TYPE = "없음" THEN FEE
ELSE ROUND(FEE * (1 - T2.DISCOUNT_RATE/100),0) END AS FEE
FROM T1
LEFT JOIN T2
ON T1.DURATION_TYPE = T2.DURATION_TYPE
ORDER BY FEE DESC, HISTORY_ID DESC
;