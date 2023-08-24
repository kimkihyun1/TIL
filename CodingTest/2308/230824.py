'''
    프로그래머스 : 숨어있는 숫자의 덧셈(2)
    https://school.programmers.co.kr/tryouts/85892/challenges?language=python3
'''

import re

def solution(my_string):
    answer = 0
    num = re.findall(r'\d+', my_string) # r'\d+' : 1번 이상 반복되는 정수
    answer = sum(list(map(int, num)))
    
    return answer

my_string = "aAb1B2cC34oOp"
print(solution(my_string))
# 37