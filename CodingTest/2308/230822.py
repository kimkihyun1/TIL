'''
    프로그래머스 : OX퀴즈
    https://school.programmers.co.kr/tryouts/85891/challenges?language=python3
'''

def solution(quiz):
    answer = []
    for q in quiz:
        sum = 0
        q_split = q.split()
        if q_split[1] == '+':
            sum = int(q_split[0]) + int(q_split[2])
        else:
            sum = int(q_split[0]) - int(q_split[2])
        if sum == int(q_split[4]):
            answer.append('O')
        else:
            answer.append('X')
    return answer

quiz = ["3 - 4 = -3", "5 + 6 = 11"]
print(solution(quiz))
# ["X", "O"]