'''
    프로그래머스 : 섬 연결하기
    https://school.programmers.co.kr/learn/courses/30/lessons/42861
'''

def solution(n, costs):
    answer = 0
    
    costs.sort(key=lambda x: x[2])
    print(costs) # [[0, 1, 1], [1, 3, 1], [0, 2, 2], [1, 2, 5], [2, 3, 8]]
    
    bridge = set([costs[0][0]])
    print(bridge) # {0}
    
    while len(bridge) != n:
        for cost in costs:
            if cost[0] in bridge and cost[1] in bridge:
                continue
            if cost[0] in bridge or cost[1] in bridge:
                bridge.update([cost[0], cost[1]]) # 중복은 제거
                answer += cost[2]
                
                print(bridge)
                print(answer)
                # {0, 1}
                # 1
                # {0, 1, 3}
                # 2
                # {0, 1, 2, 3}
                # 4
                break
    
    return answer


n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs)) # 4

# Kruskal 알고리즘의 시간 복잡도는 O(elog₂e)
