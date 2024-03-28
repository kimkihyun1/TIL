'''
    프로그래머스 : 택배 배달과 수거하기
    https://school.programmers.co.kr/tryouts/85966/challenges?language=python3
'''

def solution(cap, n, deliveries, pickups):
    total_dist = 0
    current_deliveries = 0
    current_pickups = 0
    last_stop = n
    
    for stop in range(n - 1, -1, -1):
        current_deliveries += deliveries[stop]
        current_pickups += pickups[stop]
        
        while current_deliveries > cap or current_pickups > cap:
            current_deliveries -= cap
            current_pickups -= cap
            total_dist += 2 * (last_stop) # 왕복거리계산을 위해 2배 곱한다
            last_stop = stop + 1
    
    if current_deliveries > 0 or current_pickups > 0:
        total_dist += 2 * (last_stop)
        
    return total_dist
    
cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]
print(solution(cap, n, deliveries, pickups)) # 16