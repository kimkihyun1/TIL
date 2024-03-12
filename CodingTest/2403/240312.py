'''
    프로그래머스 : 평행
    https://school.programmers.co.kr/tryouts/85956/challenges?language=python3
'''

from itertools import combinations

# 기울기
def inclination(point1, point2):
    return (point2[1] - point1[1]) / (point2[0] - point1[0])

def solution(dots):
    coms = combinations(dots, 2)
    
    for com in coms:
        another = [dot for dot in dots if dot not in com]
        if inclination(*com) == inclination(*another):
            return 1
    
    return 0

dots = [[1, 4], [9, 2], [3, 8], [11, 6]]
print(solution(dots)) # 1