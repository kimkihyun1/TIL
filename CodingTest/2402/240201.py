'''
    프로그래머스 : 타겟 넘버
    https://school.programmers.co.kr/tryouts/85939/challenges?language=python3
'''

from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0], 0])
    queue.append([-1*numbers[0], 0])
    
    while queue:
        tmp, idx = queue.popleft()
        idx += 1
        
        if idx < n:
            queue.append([tmp + numbers[idx], idx])
            queue.append([tmp - numbers[idx], idx])
        else:
            if tmp == target:
                answer += 1
    
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target)) # 5