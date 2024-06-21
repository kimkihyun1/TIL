'''
    프로그래머스 : 방의 개수
    https://school.programmers.co.kr/learn/courses/30/lessons/49190
'''

from collections import defaultdict

def solution(arrows):
    answer = 0
    visit = defaultdict(list)
    x, y = 0, 0
    dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]

    for arrow in arrows:
        for _ in range(2):  # 대각선 방향 처리를 위해 두 번 이동
            nx = x + dx[arrow]
            ny = y + dy[arrow]

            if (nx, ny) in visit and (x, y) not in visit[(nx, ny)]:
                # 새로운 위치가 이미 방문된 적이 있지만 현재 위치에서 그 위치로 가는 경로는 방문된 적이 없는 경우
                answer += 1  # 방 개수 증가
                visit[(x, y)].append((nx, ny))
                visit[(nx, ny)].append((x, y))
            elif (nx, ny) not in visit:
                # 새로운 위치가 방문된 적이 없는 경우
                visit[(x, y)].append((nx, ny))
                visit[(nx, ny)].append((x, y))

            x, y = nx, ny  # 새로운 위치로 이동
    return answer

arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]	
print(solution(arrows)) # 3