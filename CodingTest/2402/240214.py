'''
    프로그래머스 : 예산
    https://school.programmers.co.kr/tryouts/85947/challenges?language=python3
'''

def solution(d, budget):
    answer = 0
    d.sort()
    
    for i in d:
        budget -= i
        if budget < 0:
            break
        answer += 1
        
    return answer

d = [1,3,2,5,4]
budget = 9
print(solution(d, budget)) # 3
