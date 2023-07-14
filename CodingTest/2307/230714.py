'''
    프로그래머스 : 게임 맵 최단거리
'''

from collections import deque

def bfs(x, y, maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]) or maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    
    return maps[len(maps)-1][len(maps[0])-1]

def solution(maps):
    answer = bfs(0, 0, maps)
    
    if answer == 1:
        return -1
    else:
        return answer 
    
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))
# 11