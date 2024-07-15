'''
    프로그래머스 : 피로도
    https://school.programmers.co.kr/learn/courses/30/lessons/87946
'''

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for dungeon in permutations(dungeons, len(dungeons)):
        # print(dungeon)
        # ([80, 20], [50, 40], [30, 10])
        # ([80, 20], [30, 10], [50, 40])
        # ([50, 40], [80, 20], [30, 10])
        # ([50, 40], [30, 10], [80, 20])
        # ([30, 10], [80, 20], [50, 40])
        # ([30, 10], [50, 40], [80, 20])
        
        current_k = k
        cnt = 0
        
        for need, spend in dungeon:
            if current_k >= need:
                current_k -= spend
                cnt += 1
        
        answer = max(answer, cnt)
        
    return answer

k = 80
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k, dungeons)) # 3