'''
    프로그래머스 : 여행경로
    https://school.programmers.co.kr/learn/courses/30/lessons/43164
'''

from collections import deque

def solution(tickets):
    answer = []
    q = deque()
    q.append(("ICN", ["ICN"], []))
    
    while q:
        now, path, used = q.popleft()
        
        if len(used) == len(tickets):
            answer.append(path)
        
        for idx, ticket in enumerate(tickets):
            if ticket[0] == now and not idx in used:
                q.append((ticket[1], path + [ticket[1]], used + [idx]))
                
    answer.sort()
    
    return answer[0]

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets)) # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]