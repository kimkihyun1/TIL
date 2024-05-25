'''
    프로그래머스 : 징검다리
    https://school.programmers.co.kr/learn/courses/30/lessons/43236
'''

def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    start = 1
    end = distance
    
    while start <= end:
        mid = (start + end) // 2
        pre = 0
        cnt = 0
        
        for r in rocks:
            if r - pre < mid:
                cnt += 1
                if cnt > n:
                    break
            else:
                pre = r
        
        if cnt > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    
    return answer

distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
print(solution(distance, rocks, n)) # 4