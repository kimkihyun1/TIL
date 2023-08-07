'''
    프로그래머스 : 유전 법칙(PCCP)
    https://school.programmers.co.kr/tryouts/72138/challenges?language=python3
'''

def generation(query):
    n, p = query
    stack = []
    
    p -= 1
    while n > 1:
        stack.append(p % 4)
        n -= 1
        p //= 4
    
    while stack:
        num = stack.pop()
        if num == 0:
            return 'RR'
        if num == 3:
            return 'rr'
        
    return 'Rr'

def solution(queries):
    return [*map(generation, queries)]

queries = [[3, 1], [2, 3], [3, 9]]
print(solution(queries))
# ["RR", "Rr", "RR"]