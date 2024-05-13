'''
    프로그래머스 : 디스크 컨트롤러
    https://school.programmers.co.kr/learn/courses/30/lessons/42627?language=python3
'''

import heapq

def solution(jobs):
    answer = 0
    tasks = sorted([(job[1], job[0]) for job in jobs], key=lambda x: (x[1], x[0]), reverse=True) # 오름차순
    heap = []
    heapq.heappush(heap, tasks.pop())
    current_time = 0
    
    while len(heap) > 0:
        during_time, ask_time = heapq.heappop(heap)
        current_time = max(current_time+during_time, ask_time+during_time)
        answer += current_time - ask_time
        
        while len(tasks) > 0 and tasks[-1][1] <= current_time:
            heapq.heappush(heap, tasks.pop())
        if len(tasks) > 0 and len(heap) == 0:
            heapq.heappush(heap, tasks.pop())
            
    return answer // len(jobs)

    
jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))