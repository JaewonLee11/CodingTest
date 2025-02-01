SELECT 
    YEAR(DIFFERENTIATION_DATE) AS YEAR, (YEAR_MAX - SIZE_OF_COLONY) AS YEAR_DEV, ID 
FROM 
    (SELECT *,
        MAX(SIZE_OF_COLONY) OVER (PARTITION BY YEAR(DIFFERENTIATION_DATE)) AS YEAR_MAX
    FROM ECOLI_DATA) AS T
ORDER BY YEAR, YEAR_DEV
;