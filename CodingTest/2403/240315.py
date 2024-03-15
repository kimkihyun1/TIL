'''
    프로그래머스 : 공원산책
    https://school.programmers.co.kr/tryouts/85959/challenges?language=python3
'''

def solution(park, routes):
    w, h = len(park[0]), len(park)
    
    for i, v in enumerate(park):
        if 'S' in v:
            x, y = v.find('S'), i
            
    move = {'E': [0, 1], 'W': [0, -1], 'N': [-1, 0], 'S': [1, 0]}
    
    for route in routes:
        direction, step = route.split(' ')
        step = int(step)
        
        move_y, move_x = move[direction]
    
        # 범위 밖으로 나가는지 확인
        if not ((x + move_x * step) in range(w) and (y + move_y * step) in range(h)):
            continue
        
        # 장애물이 있는지 확인
        block = False
        for i in range(1, step + 1):
            if park[y + move_y * i][x + move_x * i] == 'X':
                block = True
                break
        
        if not block:
            x += move_x * i
            y += move_y * i
    
    return [y, x]

park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]
print(solution(park, routes)) # [2, 1]