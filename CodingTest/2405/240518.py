'''
    프로그래머스 : 정수 삼각형
    https://school.programmers.co.kr/learn/courses/30/lessons/43105
'''

def solution(triangle):
    floor = len(triangle) - 1
    
    # 맨 아래 부터 올라오면서 큰 수를 더한다.
    while floor > 0:
        for i in range(floor):
            triangle[floor-1][i] += max(triangle[floor][i], triangle[floor][i+1])
        
        floor -= 1
        
    return triangle[0][0]

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle)) # 30