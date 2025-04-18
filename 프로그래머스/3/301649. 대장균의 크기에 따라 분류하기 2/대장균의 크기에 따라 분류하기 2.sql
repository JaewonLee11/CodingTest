SELECT ID, 
CASE
WHEN NTILE_SIZE = 1 THEN 'CRITICAL'
WHEN NTILE_SIZE = 2 THEN 'HIGH'
WHEN NTILE_SIZE = 3 THEN 'MEDIUM'
ELSE 'LOW' END
AS COLONY_NAME
FROM (SELECT ID,
      NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC) AS NTILE_SIZE
      FROM ECOLI_DATA) RANK_DATA
ORDER BY ID;