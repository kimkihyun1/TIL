'''
    프로그래머스 : 아이템 줍기
    https://school.programmers.co.kr/learn/courses/30/lessons/87694
'''

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    size = 102
    graph = [[-1] * size for _ in range(size)]
    visited = [[0] * size for _ in range(size)]
    
    # 좌표 2배로 확대
    for rec in rectangle:
        lx, ly, rx, ry = [r*2 for r in rec]
        for x in range(lx, rx+1):
            for y in range(ly, ry+1):
                # 사각형 내부
                if lx < x < rx and ly < y < ry:
                    graph[x][y] = 0
                
                # 사각형 경계
                elif graph[x][y] != 0:
                    graph[x][y] = 1
        
    # 방향 이동
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(characterX*2, characterY*2)])
    
    while queue:
        x, y = queue.popleft()
        
        # 아이템 위치 도착
        if (x, y) == (itemX*2, itemY*2):
            return visited[x][y] // 2
        
        # 방향 이동
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 < nx < size and 0 < ny < size and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))    
    

rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
characterX = 1
characterY = 3
itemX = 7
itemY = 8
print(solution(rectangle, characterX, characterY, itemX, itemY)) # 17