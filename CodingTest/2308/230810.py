'''
    프로그래머스 : 운영체제(PCCP)
    https://school.programmers.co.kr/tryouts/72139/challenges?language=python3
'''

from queue import PriorityQueue

def call(program, cursor, q):
    while program and program[0][1] <= cursor:
        q.put(program.pop(0))

def solution(program):
    answer = [0 for _ in range(10)]
    program.sort(key=lambda x: x[1])
    q = PriorityQueue()
    cursor = 0
    
    while program or q.empty() == False:
        if q.empty():
            cursor = program[0][1]
        else:
            execute = q.get()
            answer[execute[0] - 1] += cursor - execute[1]
            cursor += execute[2]
            
        call(program, cursor, q)
        
    return [cursor, *answer]

program = [[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]
print(solution(program))
# [20, 5, 0, 16, 0, 0, 0, 0, 0, 0, 0]