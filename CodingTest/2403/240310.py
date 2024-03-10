'''
    프로그래머스 : 정수 삼각형
    https://school.programmers.co.kr/tryouts/85954/challenges?language=python3
'''

def solution(triangle):
    answer = 0
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0: # 맨 왼쪽
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1: # 맨 오른쪽
                triangle[i][j] += triangle[i-1][-1]
            else: # 가운데
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    answer = max(triangle[-1])
    
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))