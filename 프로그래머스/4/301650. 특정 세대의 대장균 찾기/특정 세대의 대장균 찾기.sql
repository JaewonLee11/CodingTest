SELECT ID FROM ECOLI_DATA
WHERE PARENT_ID IN (SELECT ID FROM ECOLI_DATA WHERE
PARENT_ID IN (SELECT ID FROM ECOLI_DATA WHERE PARENT_ID IS NULL GROUP BY ID)
GROUP BY ID)
GROUP BY ID
ORDER BY ID
;