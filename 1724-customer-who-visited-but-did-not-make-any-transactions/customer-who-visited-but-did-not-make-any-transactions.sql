# Write your MySQL query statement below
# Write your MySQL query statement below
SELECT DISTINCT(C.CUSTOMER_ID), COUNT(C.VISIT_ID) AS count_no_trans 
FROM VISITS C WHERE C.VISIT_ID NOT IN(
SELECT V.VISIT_ID FROM VISITS V 
JOIN TRANSACTIONS T ON V.VISIT_ID=T.VISIT_ID
) GROUP BY C.CUSTOMER_ID;