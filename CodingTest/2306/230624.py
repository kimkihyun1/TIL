'''
    프로그래머스 : 섬 연결하기
'''

def solution(n, costs):
    answer = 0
    costs.sort(key= lambda x : x[2]) # 연결 비용이 적은 순으로 오름차순
    link = set([costs[0][0]])
    
    while len(link) != n:
        for v in costs:
            if v[0] in link and v[1] in link:
                continue
            if v[0] in link or v[1] in link:
                link.update([v[0], v[1]])
                answer += v[2]
                break
    
    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))
# 4