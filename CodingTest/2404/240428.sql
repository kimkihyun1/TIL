/*
    프로그래머스 : 조건에 맞는 사용자와 총 거래금액 조회하기
    https://school.programmers.co.kr/learn/courses/30/lessons/164668
*/

SELECT U.USER_ID, U.NICKNAME, SUM(B.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS B
JOIN USED_GOODS_USER AS U ON B.WRITER_ID = U.USER_ID
WHERE B.STATUS = 'DONE'
GROUP BY B.WRITER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES