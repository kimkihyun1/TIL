'''
    프로그래머스 : 수식 최대화(카카오)
'''

from itertools import permutations

# 연산 
def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))

def cal(exp, op):
    array = []
    tmp =""
    for i in exp:
        if i.isdigit():
            tmp += i
        else:
            array.append(tmp)
            array.append(i)
            tmp = ""
    array.append(tmp)  # 수식을 배열로 표현
    
    for j in op:
        stack = []
        while len(array) != 0:
            tmp = array.pop(0)
            if tmp == j:
                stack.append(operation(stack.pop(), array.pop(0), j))
            else:
                stack.append(tmp)
        array = stack
    return abs(int(array[0]))        

def solution(expression):
    op = ['+', '-', '*']
    op = list(permutations(op, 3))
    answer = []
    for i in op:
        answer.append(cal(expression, i))
    return max(answer)

expression = "100-200*300-500+20"
print(solution(expression))
# 60420