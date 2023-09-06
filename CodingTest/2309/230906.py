'''
    프로그래머스 : 치킨 쿠폰
    https://school.programmers.co.kr/tryouts/85900/challenges?language=python3
'''

def solution(chicken):
    answer = 0
    while chicken >= 10:
        div, mod = divmod(chicken, 10)
        answer += div
        chicken = div + mod
        
    return answer

chicken = 100
print(solution(chicken))
# 11