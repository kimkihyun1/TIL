'''
    프로그래머스 : 명예의 전당(1)
    https://school.programmers.co.kr/tryouts/85933/challenges?language=python3
'''

def solution(k, score):
    answer = []
    tmp = []
    
    for s in score:
        if len(tmp) < k:
            tmp.append(s)
        else:
            if min(tmp) < s:
                tmp.remove(min(tmp))
                tmp.append(s)
        answer.append(min(tmp))
        
    return answer

k = 3
score = [10, 100, 20, 150, 1, 100, 200]
print(solution(k, score)) # [10, 10, 10, 20, 20, 100, 100]