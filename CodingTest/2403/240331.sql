/*
    프로그래머스 : 3월에 태어난 여성 회원 목록 출력하기
    https://school.programmers.co.kr/learn/courses/30/lessons/131120
*/

SELECT MEMBER_ID, MEMBER_NAME, 	GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH)=3 AND GENDER='W' AND TLNO IS NOT NULL
ORDER BY MEMBER_ID;

-- DATE_FORMAT에서 %m-%d를 써야 월과 일이 숫자로 출력된다