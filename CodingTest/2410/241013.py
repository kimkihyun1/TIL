'''
    프로그래머스 : 모음 사전
    https://school.programmers.co.kr/learn/courses/30/lessons/84512
'''

from itertools import product 

def solution(word):
    answer = 0
    words = []
    for i in range(1,6):
        # 중복 순열로 모든 알파벳 조합
        for w in product('AEIOU', repeat=i): 
            words.append(''.join(list(w)))
    
    words.sort()
    answer = words.index(word) +1
    
    return answer
            
word = "AAAE"
print(solution(word)) # 10