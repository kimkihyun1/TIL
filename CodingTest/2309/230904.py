'''
    프로그래머스 : 연속된 수의 합
    https://school.programmers.co.kr/tryouts/85899/challenges?language=python3
'''

def solution(num, total):
    answer = []
    var = sum(range(num+1))
    diff = total - var
    start = diff // num
    answer = [start + 1 + i for i in range(num)]
    
    return answer

num = 3
total = 12
print(solution(num, total))
# [3, 4, 5]