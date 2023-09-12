'''
    프로그래머스 : 369게임
    https://school.programmers.co.kr/tryouts/85902/challenges?language=python3
'''

def solution(order):
    answer = 0
    for i in str(order):
        if i in ['3', '6', '9']:
            answer += 1
    return answer

order = 29423
print(solution(order))
# 2