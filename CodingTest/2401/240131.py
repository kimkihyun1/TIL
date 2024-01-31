'''
    프로그래머스 : 네트워크
    https://school.programmers.co.kr/tryouts/85938/challenges?language=python3
'''

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    
    for i in range(n):
        if visited[i] == False:
            DFS(n, computers, i, visited)
            answer += 1
    
    return answer

def DFS(n, computers, i, visited):
    visited[i] = True
    
    for conn in range(n):
        if conn != i and computers[i][conn] == 1:
            if visited[conn] == False:
                DFS(n, computers, conn, visited)
                
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers)) # 2