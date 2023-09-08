'''
    프로그래머스 : k의 개수
    https://school.programmers.co.kr/tryouts/85901/challenges?language=python3
'''

def solution(i, j, k):
    answer = 0
    
    for num in range(i, j+1):
        if str(k) in str(num):
            answer += str(num).count(str(k))
    return answer

i = 1
j = 13
k = 1
print(solution(i, j, k))
# 6