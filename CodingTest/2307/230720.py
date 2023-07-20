'''
    프로그래머스 : 단속카메라
'''

def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # 진출 기준으로 정렬
    camera = -30001 # 최소 진입지점보다 1작게 설정
    
    for route in routes:
        if camera < route[0]:
            camera = route[1] # 진출을 기준으로
            answer += 1
    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))
# 2