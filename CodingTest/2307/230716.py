'''
    프로그래머스 : 경주로 건설(카카오)
'''

from heapq import heappop, heappush
from sys import maxsize

def solution(board):
    n = len(board)
    costTable = [[[maxsize] * n for _ in range(n)] for _ in range(4)]
    for i in range(4):
        costTable[i][0][0] = 0
    
    heap = [(0, 0, 0, 0), (0, 0, 0 ,2)]
    while heap:
        cost, x, y ,d = heappop(heap)
        for dx, dy, dist in ((1,0,0), (-1,0,1), (0,1,2), (0,-1,3)):
            nx, ny = x + dx, y + dy
            
            if nx < 0 or ny < 0 or nx >=n or ny >= n or board[ny][nx]:
                continue
            
            if d == dist:
                newcost = cost + 100
            else:
                newcost = cost + 600
            
            if costTable[dist][ny][nx] > newcost:
                costTable[dist][ny][nx] = newcost
                heappush(heap, (newcost, nx, ny, dist))

    return min(costTable[0][n-1][n-1], costTable[1][n-1][n-1], costTable[2][n-1][n-1], costTable[3][n-1][n-1])

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(board))
# 3800