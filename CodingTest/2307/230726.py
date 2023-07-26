'''
    프로그래머스 : 양궁대회(카카오)
'''

def solution(n, info):
    apeach_score = sum(10-i for i in range(10) if info[i])
    score = [(10-i)*2 if info[i] else 10-i for i in range(10)]
    queue = [[0]]
    answer = []
    
    if n >= info[0] + 1:
        queue.append([info[0] + 1])
        
    while queue:
        recent = queue.pop(0)
        if sum(recent) == n or len(recent) == 10:
            new = sum([score[i] for i in range(len(recent)) if recent[i]])
            old = sum([score[i] for i in range(len(answer)) if answer[i]])
            if new > apeach_score and new >= old:
                answer = recent
        elif sum(recent) + info[len(recent)] + 1 <= n:
            queue.append(recent + [info[len(recent)] + 1])
            queue.append(recent + [0])
        else:
            queue.append(recent + [0])
            
    if not answer:
        return [-1]
    
    return answer + [0] * (10 - len(answer)) + [n - sum(answer)]

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n, info))
# [0,2,2,0,1,0,0,0,0,0,0]