'''
    프로그래머스 : 자릿수 더하기
    https://school.programmers.co.kr/tryouts/85895/challenges?language=python3
'''

def solution(n):
    answer = 0
    n = str(n)
    for i in n:
        answer += int(i)
        
    return answer

n = 1234
print(solution(n))
# 10