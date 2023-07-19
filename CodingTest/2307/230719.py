'''
    프로그래머스 : 구명보트
'''

def solution(people, limit):
    answer = 0
    start = 0
    end = len(people) - 1
    people.sort()
    
    while start < end:
        if people[start] + people[end] <= limit:
            start += 1
            answer += 1
        end -= 1
    
    return len(people) - answer  # answer값을 빼는 이유 2명이 보트에 탔기 때문에
                                 # 전체에서 1씩 더한 값인 answer을 빼준다
people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))
# 3