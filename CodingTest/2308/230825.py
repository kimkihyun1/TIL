'''
    프로그래머스 : 인덱스 바꾸기
    https://school.programmers.co.kr/tryouts/85893/challenges?language=python3
'''

def solution(my_string, num1, num2):
    answer = ''
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    answer = ''.join(my_string)
    
    return answer

my_string = 'hello'
num1 = 1
num2 = 2
print(solution(my_string))
# hlelo