'''
    프로그래머스 : 덧칠하기
    https://school.programmers.co.kr/tryouts/85958/challenges?language=python3
'''

def solution(n, m, section):
    answer = 0
    point = 0
    
    for i in section:
        if point < i:
            point = m + i - 1
            answer += 1
            
    return answer

n = 8
m = 4
section = [2, 3, 6] 
print(solution(n, m, section)) # 2