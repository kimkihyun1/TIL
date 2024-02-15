'''
    프로그래머스 : 실패율
    https://school.programmers.co.kr/tryouts/85948/challenges?language=python3
'''

def solution(N, stages):
    answer = []
    user = len(stages)
    dic_fail = {}
    
    for i in range(1, N+1):
        if user != 0:
            dic_fail[i] = stages.count(i) / user
            user -= stages.count(i)
        else:
            dic_fail[i] = 0
    
    answer = sorted(dic_fail, key=lambda x: dic_fail[x], reverse=True)
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages)) # [3,4,2,1,5]