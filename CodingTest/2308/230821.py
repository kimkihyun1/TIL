'''
    프로그래머스 : 문자열 계산하기
    https://school.programmers.co.kr/tryouts/85890/challenges?language=python3
'''

def solution(my_string):
    my_string = my_string.split()
    answer = int(my_string[0])
    for i in range(1, len(my_string), 2):
        if my_string[i] == '+':
            answer += int(my_string[i+1])
        else:
            answer -= int(my_string[i+1])
    
    return answer

my_string = "3 + 4"
print(solution(my_string))
# 7