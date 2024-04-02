'''
    프로그래머스 : 더 맵게
    https://school.programmers.co.kr/learn/courses/30/lessons/42626
'''

import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    
    for s in scoville:
        heapq.heappush(heap, s)
    
    while heap[0] < K:
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        answer += 1
        
        if len(heap) == 1 and heap[0] < K:
            return -1
    
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K)) # 2