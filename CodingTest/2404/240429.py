'''
    프로그래머스 : 가장 먼 노드
    https://school.programmers.co.kr/learn/courses/30/lessons/49189
'''

from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)] # 연결된 노드 그래프 리스트
    dist = [-1] * (n+1) # 노드들의 최단거리 리스트
    
    # 노드 정보 추가
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    # graph = [[], [3, 2], [3, 1, 4, 5], [6, 4, 2, 1], [3, 2], [2], [3]]

    queue = deque([1]) # 출발 노드 : 1
    dist[1] = 0 # 출발노드의 최단 거리 : 0
    
    # BFS
    while queue:
        now = queue.popleft() # 현재 노드
        
        for i in graph[now]:
            if dist[i] == -1: # 방문하지 않은 노드
                queue.append(i)
                dist[i] = dist[now] + 1 # 최단거리 갱신
    
    # 가장 멀리 떨어진 노드 거리
    for d in dist: 
        if d == max(dist):
            answer += 1 
        
    return answer

n = 6
edge = 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge)) # 3