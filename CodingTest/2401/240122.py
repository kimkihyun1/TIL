'''
    프로그래머스 : 더 맵게
    https://school.programmers.co.kr/tryouts/85934/challenges?language=python3
'''

import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    
    for s in scoville:
        heapq.heappush(heap, s)
        
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2) # heappush 이후 자동으로 정렬
        except IndexError:
            return -1
        answer += 1
        
    return answer
        
scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K)) # 2