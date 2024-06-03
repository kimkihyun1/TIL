'''
    프로그래머스 : 올바른 괄호
    https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3
'''

def solution(s):
    answer = True
    stack = []
    
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        else:
            if stack == []: # 첫 문자가 ')' 일 시
                return False
            else:
                stack.pop()
    
    if stack: # 스택이 비어 있지 않으면
        return False

    return answer

s = "(()("
print(solution(s)) # False