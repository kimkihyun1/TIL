'''
    프로그래머스 : 캐릭터의 좌표
    https://school.programmers.co.kr/tryouts/85957/challenges?language=python3
'''

def in_board(x, y, width, height):
    return -width <= x <= width and -height <= y <= height

def solution(keyinput, board):
    answer = [0, 0]
    width = board[0] // 2
    height = board[1] // 2
    
    for i in keyinput:
        if i == "left":
            move = [-1, 0]
        elif i == "right":
            move = [1, 0]
        elif i == "up":
            move = [0, 1]
        elif i == "down":
            move = [0, -1]
    
        if in_board(answer[0] + move[0], answer[1] + move[1], width, height):
            answer[0] += move[0]
            answer[1] += move[1]
    
    return answer

keyinput = ["down", "down", "down", "down", "down"]
board = [7, 9]
print(solution(keyinput, board))