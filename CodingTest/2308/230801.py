'''
    프로그래머스 : 사라지는 발판(카카오)
    https://school.programmers.co.kr/tryouts/72135/challenges?language=python3
'''

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def in_range(board, y ,x):
    if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]):
        return False
    return True

def finished(board, y ,x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if in_range(board, ny, nx) and board[ny][nx]:
            return False
    return True

def solve(board, y1, x1, y2, x2):
    if finished(board, y1, x1):
        return [False, 0]
    
    if y1 == y2 and x1 == x2:
        return [True, 1]
    
    min_turn = 100
    max_turn = 0
    can_win = False
    
    for i in range(4):
        ny = y1 + dy[i]
        nx = x1 + dx[i]
        if not in_range(board, ny, nx) or not board[ny][nx]:
            continue
        
        board[y1][x1] = 0
        result = solve(board, y2, x2, ny, nx)
        board[y2][x2] = 1
        
        if not result[0]:
            can_win = True
            min_turn = min(min_turn, result[1])
        elif not can_win:
            max_turn = max(max_turn, result[1])
    
    turn = min_turn if can_win else max_turn
    
    return [can_win, turn + 1]

def solution(board, aloc, bloc):
    return solve(board, aloc[0], aloc[1], bloc[0], bloc[1])[1]

board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1,0]
bloc = [1, 2]
print(solution(board, aloc, bloc))
# 5