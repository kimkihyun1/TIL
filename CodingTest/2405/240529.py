'''
    프로그래머스 : 순위
    https://school.programmers.co.kr/learn/courses/30/lessons/49191?language=python3
'''

from collections import defaultdict

def solution(n, results):
    answer = 0
    win_graph = defaultdict(set)
    lose_graph = defaultdict(set)
    
    for win, lose in results:
        win_graph[lose].add(win)
        lose_graph[win].add(lose)
    
    print(win_graph) # {3: {4}, 2: {1, 3, 4}, 5: {2}}
    print(lose_graph) # {4: {2, 3}, 3: {2}, 1: {2}, 2: {5}}       
    for i in range(1, n+1):
        for win in win_graph[i]:
            lose_graph[win].update(lose_graph[i])
        for lose in lose_graph[i]:
            win_graph[lose].update(win_graph[i])
    print(win_graph) # {3: {4}, 2: {1, 3, 4}, 5: {1, 2, 3, 4}, 1: set(), 4: set()}
    print(lose_graph) # {4: {2, 3, 5}, 3: {2, 5}, 1: {2, 5}, 2: {5}, 5: set()}
    
    for i in range(1, n+1):
        if len(win_graph[i]) + len(lose_graph[i]) == n - 1:
            answer += 1
    
        
    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	
print(solution(n, results)) # 2