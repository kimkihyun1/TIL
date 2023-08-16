'''
    프로그래머스 : 카페 확장(PCCP)
    https://school.programmers.co.kr/tryouts/72142/challenges
'''

from collections import deque

def solution(menu, order, k):
    answer = 1
    enter = deque([x * k for x in range(len(order))])
    q = deque([enter.popleft()])
    curr = 0
    
    for i in range(len(order)):
        curr = max(curr, i * k) + menu[order[i]]
        while enter and enter[0] < curr:
            q.append(enter.popleft())
            
        answer = max(answer, len(q))
        q.popleft()
        
        if enter and enter[0] == curr:
            q.append(enter.popleft())
        
    return answer

menu = [5, 12, 30]
order = [1, 2, 0, 1]
k = 10
print(solution(menu, order, k))
# 3