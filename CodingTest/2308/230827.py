'''
    프로그래머스 : 문자열 밀기
    https://school.programmers.co.kr/tryouts/85894/challenges?language=python3
'''

def solution(A, B):
    answer = -1
    if A == B:
        return 0
    for i in range(len(A)):
        move_word = A[len(A) - i:] + A[:len(A) - i]
        print(move_word)
        if move_word == B:
            return i
    
    return answer


A = 'hello'
B = 'ohell'
print(solution(A, B))
# 1