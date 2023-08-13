'''
    프로그래머스 : 신입사원 교육(PCCP)
    https://school.programmers.co.kr/tryouts/72141/challenges?language=python3
'''

from heapq import heapify, heappop, heappush

def solution(ability, number):
    heapify(ability)
    for i in range(number):
        first = heappop(ability)
        second = heappop(ability)
        heappush(ability, first + second)
        heappush(ability, first + second)
    
    return sum(ability)

ability = [10, 3, 7, 2]
number = 2
print(solution(ability, number))
# 37