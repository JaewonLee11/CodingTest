-- 코드를 입력하세요
SELECT INS.ANIMAL_ID, INS.NAME 
FROM ANIMAL_INS INS
LEFT JOIN ANIMAL_OUTS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE OUTS.DATETIME IS NOT NULL AND INS.DATETIME-OUTS.DATETIME > 0
ORDER BY INS.DATETIME
;