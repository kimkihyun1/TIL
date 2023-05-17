'''
    프로그래머스 : 모음 사전
    product 함수 : 중복 순열 
    참고 : https://stackstackstack.tistory.com/entry/python-%EC%88%9C%EC%97%B4-%EC%A1%B0%ED%95%A9-%ED%95%A8%EC%88%98-product-permutations-combinations
'''
from itertools import product

def solution(word):
    answer = []
    alpha = ['A', 'E', 'I', 'O', 'U']
    for i in range(1, 6):
        for j in product(alpha, repeat=i):
            answer.append(''.join(j))
    
    answer.sort()
    return answer.index(word) + 1

word = "AAAAE"
print(solution(word))
# 6