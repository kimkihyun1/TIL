'''
    프로그래머스 : 이중우선순위큐
    https://school.programmers.co.kr/learn/courses/30/lessons/42628
'''

from heapq import heappush, heappop

def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    
    for op in operations:
        operation, num = op.split()
        
        if operation == 'I':
            num = int(num)
            heappush(min_heap, num)
            heappush(max_heap, (-1*num, num))
        else:
            if num == "-1":
                if min_heap: # 힙이 비어있지 않으면
                    min_num = heappop(min_heap)
                    max_heap.remove((min_num*-1, min_num)) # 최대 힙에서 해당 값을 삭제
            else:
                if max_heap:
                    max_num = heappop(max_heap)[1]
                    min_heap.remove(max_num) # 최소 힙에서 해당 값을 삭제
    
    if min_heap == []:
        answer = [0, 0]
    else:
        answer = [heappop(max_heap)[1], heappop(min_heap)]
    
    return answer

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations)) # [333, -45]