WITH A AS (
    SELECT MEMBER_ID 
    FROM REST_REVIEW 
    GROUP BY MEMBER_ID 
    ORDER BY COUNT(MEMBER_ID) DESC 
    LIMIT 1
)

SELECT P.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
FROM REST_REVIEW R
JOIN MEMBER_PROFILE P
ON R.MEMBER_ID = P.MEMBER_ID
WHERE R.MEMBER_ID = (SELECT * FROM A)
ORDER BY REVIEW_DATE, REVIEW_TEXT
;