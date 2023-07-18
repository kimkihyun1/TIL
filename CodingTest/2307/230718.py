'''
    프로그래머스 : 큰 수 만들기
'''

def solution(number, k):
    answer = []
    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)
    
    return ''.join(answer[:len(answer)-k])

number = "1924"
k = 2
print(solution(number, k))
# "94"