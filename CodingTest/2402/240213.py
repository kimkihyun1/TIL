'''
    프로그래머스 : 진료 순서 정하기
    https://school.programmers.co.kr/tryouts/85946/challenges
'''

def solution(emergency):
    answer = []
    emer_sort = sorted(emergency, reverse=True)
    
    for i in emergency:
        answer.append(emer_sort.index(i) + 1)
    
    return answer

emergency = [30, 10, 23, 6, 100]
print(solution(emergency)) # [2, 4, 3, 5, 1]