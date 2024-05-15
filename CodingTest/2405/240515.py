'''
    프로그래머스 : 가장 큰 수
    https://school.programmers.co.kr/learn/courses/30/lessons/42746?language=python3
'''

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    # print([i*3 for i in numbers]) ['333', '303030', '343434', '555', '999']
    
    numbers.sort(key=lambda x: x*3, reverse=True) 
    # print(numbers) ['9', '5', '34', '3', '30']
    
    for num in numbers:
        answer += num
    
    # '00'이 나올경우 '0'으로 출력되어야 하기 때문에 int로 변환 후 str로 변환
    return str(int(answer)) 

numbers = [3, 30, 34, 5, 9]
print(solution(numbers)) # "9534330"