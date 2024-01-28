'''
    프로그래머스 : 야근 지수
    https://school.programmers.co.kr/tryouts/85935/challenges?language=python3
'''

import heapq

def solution(n, works):
    answer = 0
    
    if n >= sum(works):
        return answer
    
    # 음수로 변환한 후 heapify를 사용하여 최소 힙으로 변환한다
    works = [-work for work in works]
    heapq.heapify(works) 
    for _ in range(n):
        work = heapq.heappop(works) # 제일 작은 수를 꺼내어 1증가 시킨다.
        work += 1
        heapq.heappush(works, work)
    
    answer = sum([work ** 2 for work in works])
    
    return answer

n = 4
works = [4, 3, 3]
print(solution(n, works)) # 12