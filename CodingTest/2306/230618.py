'''
    프로그래머스 : 순위
'''

from collections import defaultdict

def solution(n, results):
    answer = 0
    win_graph = defaultdict(set)   # 이긴 사람
    lose_graph = defaultdict(set)   # 진 사람
    
    for win, lose in results:   # 그래프화
        win_graph[lose].add(win)    
        lose_graph[win].add(lose)
        
    for i in range(1, n+1):
        for win in win_graph[i]:
            lose_graph[win].update(lose_graph[i])   # i한테 진 사람들은 i를 이긴 사람들한테도 진 것
        for lose in lose_graph[i]:
            win_graph[lose].update(win_graph[i])    # i한테 이긴 사람들은 i한테 진 사람들한데도 이긴 것
            
    for i in range(1, n+1):
        if len(win_graph[i]) + len(lose_graph[i]) == n-1:   # i한테 이기고 진 사람들이 합쳐서 n-1이면 순위가 결정
            answer += 1
    
    return answer    
            
n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))
# 2