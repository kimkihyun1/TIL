'''
    프로그래머스 : 보물 지도(PCCP)
    https://school.programmers.co.kr/tryouts/72143/challenges?language=python3
'''

from collections import deque

def solution(n, m, hole):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    board = [[0]*m for _ in range(n)]
    
    for i, j  in hole:
        board[i-1][j-1] = 1
    
    queue = deque()
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][False] = True
    queue.append((0, 0, False))
    
    while queue:
        for _ in range(len(queue)):
            x, y, used = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][used] and board[nx][ny] == 0:
                    if (nx, ny) == (n-1, m-1):
                        return answer + 1
                    visited[nx][ny][used] = True
                    queue.append((nx, ny, used))
                if not used:
                    nx += dx[i]
                    ny += dy[i]
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][True] and board[nx][ny] == 0:
                        if (nx, ny) == (n-1, m-1):
                            return answer + 1
                        visited[nx][ny][True] = True
                        queue.append((nx, ny, True))
        
        answer += 1
        
    return -1
                        
n = 4
m = 4
hole = [[2, 3], [3, 3]]
print(solution(n, m, hole))
# 5