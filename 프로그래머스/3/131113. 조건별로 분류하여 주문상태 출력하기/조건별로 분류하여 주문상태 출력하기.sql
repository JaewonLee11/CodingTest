-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID, DATE_FORMAT(OUT_DATE,"%Y-%m-%d") AS OUT_DATE, 
CASE
WHEN DATE_FORMAT(OUT_DATE,"%Y-%m-%d") < "2022-05-11" THEN "출고완료"
WHEN DATE_FORMAT(OUT_DATE,"%Y-%m-%d") >= "2022-05-11" THEN "출고대기"
WHEN DATE_FORMAT(OUT_DATE,"%Y-%m-%d") IS NULL THEN "출고미정" END
AS 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID
;