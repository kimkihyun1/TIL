'''
    프로그래머스 : 실습용 로봇(PCCP)
    https://school.programmers.co.kr/tryouts/72140/challenges?language=python3
'''

def solution(command):
    path = [[0,1], [1,0], [0,-1], [-1,0]]
    x = 0
    y = 0
    d = 0
    
    for i in command:
        if i == 'R':
            d = (d+1) % 4
        elif i == 'L':
            d = (d+3) % 4
        elif i == 'G':
            x += path[d][0]
            y += path[d][1]
        else:
            x -= path[d][0]
            y -= path[d][1]
            
    return [x, y]

command = "GRGLGRG"
print(solution(command))
# 	[2, 2]