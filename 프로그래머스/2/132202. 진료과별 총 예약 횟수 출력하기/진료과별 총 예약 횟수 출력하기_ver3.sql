SELECT 
    MCDP_CD AS "진료과코드", 
    COUNT(PT_NO) AS "5월예약건수"
FROM 
    APPOINTMENT
WHERE 
    APNT_YMD BETWEEN TO_DATE('2022-05-01', 'YYYY-MM-DD') AND TO_DATE('2022-05-31', 'YYYY-MM-DD')
GROUP BY 
    MCDP_CD
ORDER BY 
    COUNT(PT_NO) ASC, 
    MCDP_CD ASC;
