'''
    프로그래머스 : 징검 다리
'''

def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    rocks.append(distance)
    rocks.sort()
    
    while start <= end:
        mid = (start+end) // 2
        del_stone = 0   # 제거한 돌 갯수
        st_stone = 0    # 기준이 되는 돌
        min_distnace = float('inf')
        
        for rock in rocks:
            dis = rock - st_stone
            if dis < mid:
                del_stone += 1
            else:
                st_stone = rock
                min_distnace = min(min_distnace, dis)  # 최소값

        
        if del_stone > n:   # 제거된 돌이 많으므로 범위를 줄인다.
            end = mid - 1
        else:
            answer = min_distnace
            start = mid + 1
            
    return answer

distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2

print(solution(distance, rocks, n))