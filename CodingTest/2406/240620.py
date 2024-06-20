'''
    프로그래머스 : 게임 맵 최단거리
    https://school.programmers.co.kr/learn/courses/30/lessons/1844
'''

from collections import deque

def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 맵 바깥일시
                if nx < 0 or nx >= len(maps[0]) or ny < 0 or ny >= len(maps):
                    continue
                
                # 벽 일시
                if maps[ny][nx] == 0:
                    continue
                    
                if maps[ny][nx] == 1:
                    maps[ny][nx] = maps[y][x] + 1
                    queue.append((nx, ny))
                    
        return maps[len(maps)-1][len(maps[0])-1]
    
    answer = bfs(0, 0)
    return -1 if answer == 1 else answer 

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	
print(solution(maps)) # 11