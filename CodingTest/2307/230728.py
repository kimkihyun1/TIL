'''
    프로그래머스 : 양과 늑대(카카오)
'''

def dfs(sheep, wolf, info, edges, answer, visited):
    if sheep > wolf:
        answer.append(sheep)
    else:
        return 
    
    for p, c in edges:
        if visited[p] and not visited[c]:
            visited[c] = 1
            if info[c] == 0:
                dfs(sheep+1, wolf, info, edges, answer, visited)
            else:
                dfs(sheep, wolf+1, info, edges, answer, visited)
            visited[c] = 0

def solution(info, edges):
    answer = []
    visited = [0] * len(info)
    visited[0] = 1
    dfs(1, 0, info, edges, answer, visited)
    
    return max(answer)

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution(info, edges))
# 5