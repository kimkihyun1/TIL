'''
    프로그래머스 : 베스트 앨범
'''

def solution(genres, plays):
    answer = []
    
    dic = {}
    dic_sum = {}
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic:
            dic[g] = [(i, p)]
        else:
            dic[g].append((i, p))
            
        if g not in dic_sum:
            dic_sum[g] = p
        else:
            dic_sum[g] += p
    
    for (k, v) in sorted(dic_sum.items(), key=lambda x:x[1], reverse=True):
        # print(k, v)
        for (i, p) in sorted(dic[k], key=lambda x: x[1], reverse=True)[:2]:
            # print(i, p)
            answer.append(i)
    
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 500, 2500]
print(solution(genres, plays))