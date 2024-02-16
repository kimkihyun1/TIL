'''
    프로그래머스 : 개미 군단
    https://school.programmers.co.kr/tryouts/85949/challenges?language=python3
'''

def solution(hp):
    answer = 0
    ant_5 = 5
    ant_3 = 3
    ant_1 = 1
    
    while hp > 0:
        if hp >= 5:
            hp -= ant_5
            answer += 1
        elif hp >= 3:
            hp -= ant_3
            answer += 1
        else:
            hp -= ant_1
            answer += 1
            
    return answer

hp = 23
print(solution(hp)) # 5