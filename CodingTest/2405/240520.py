'''
    프로그래머스 : 네트워크
    https://school.programmers.co.kr/learn/courses/30/lessons/43162
'''

def solution(n, computers):
    def DFS(i):
        visited[i] = True
        
        for j in range(n):
            # 방문하지 않았고 computers[i][j]가 1이면 
            if not visited[j] and computers[i][j]:
                DFS(j)
    
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            DFS(i)
            answer += 1 # 더 이상 연결되지 않으면 함수를 빠져나와 +1
    
    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers)) # 2