'''
    프로그래머스 : 큰 수 만들기
    https://school.programmers.co.kr/learn/courses/30/lessons/42883
'''

def solution(number, k):
    answer = []
    
    for n in number:
        while len(answer) > 0 and k > 0 and answer[-1] < n:
            answer.pop()
            k -= 1
        answer.append(n)    
        
    if k:
        return number[:-k]
    return ''.join(answer)
    
number = "4177252841"
k = 4
print(solution(number, k)) # "775841"