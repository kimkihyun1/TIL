'''
    프로그래머스 : 구명보트
    https://school.programmers.co.kr/learn/courses/30/lessons/42885
'''

def solution(people, limit):
    answer = 0
    people.sort()
    
    start = 0
    end = len(people) - 1
    
    while start < end:
        if people[start] + people[end] <= limit:
            start += 1
            answer += 1
        end -= 1
        
    return len(people) - answer

people = [70, 50, 80, 50]	
limit = 100
print(solution(people, limit)) # 3