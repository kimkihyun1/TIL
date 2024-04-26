'''
    프로그래머스 : 입국심사
    https://school.programmers.co.kr/learn/courses/30/lessons/43238?language=python3
'''

def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        people = 0
        
        for time in times:
            people += mid // time
            
            if people >= n:
                break
                
        if people >= n:
            answer = mid
            right = mid - 1
        
        else:
            left = mid + 1
    
    return answer

n = 6
times = [7, 10]
print(solution(n, times)) # 28