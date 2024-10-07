'''
    프로그래머스 : 단속카메라
    https://school.programmers.co.kr/learn/courses/30/lessons/42884
'''

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) 
    # routes : [[-20, -15], [-18, -13], [-14, -5], [-5, -3]]
    camera = -30001 # 최소값으로 초기화
    
    for route in routes:
        if camera < route[0]: # 진입 지점이 크면
            answer +=1
            camera = route[1] # 진출 지점으로 갱신
    
    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	
print(solution(routes)) # 2