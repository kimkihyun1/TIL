'''
    프로그래머스 : 안전지대
    https://school.programmers.co.kr/tryouts/85955/challenges?language=python3
'''

def solution(board):
    answer = 0
    n = len(board)
    danger = set()
    
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val:
                danger.update(
                (i + di, j + dj)
                for di in [-1, 0, 1]
                for dj in [-1, 0, 1]
                if 0 <= i + di < n and 0 <= j + dj < n
                )
    
    answer = n * n - len(danger)
    
    return answer

board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
print(solution(board))