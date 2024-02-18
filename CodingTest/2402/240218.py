'''
    프로그래머스 : 단속카메라
    https://school.programmers.co.kr/tryouts/85951/challenges?language=python3
'''

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    cam = -30001
    
    for i in routes:
        if cam < i[0]:
            cam = i[1]
            answer += 1
        
    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes)) # 2