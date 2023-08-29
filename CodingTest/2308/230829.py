'''
    프로그래머스 : 문자열 나누기
    https://school.programmers.co.kr/tryouts/85896/challenges?language=python3
'''

def solution(s):
    answer = 0
    same_word = 0
    not_same_word = 0
    for w in s:
        if same_word == not_same_word:
            first_word = w
            answer += 1
        if first_word == w:
            same_word += 1
        else:
            not_same_word += 1
    
    return answer

s = "banana"
print(solution(s))
# 3