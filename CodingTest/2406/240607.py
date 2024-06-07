'''
    프로그래머스 : 소수 찾기
    https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=python3
'''

from itertools import permutations

def solution(numbers):
    answer = []
    num_str = [n for n in numbers]
    num_per = []
    
    for i in range(1, len(numbers) + 1):
        num_per += list(permutations(num_str, i)) # 순열 조합
    
    # str -> int 형 변환
    num_int = [int("".join(n)) for n in num_per] 
    
    for n in num_int:
        if n < 2:
            continue
        
        check = True
        # 소수 찾기
        for i in range(2, int(n**0.5)+1): 
            if n % i == 0:
                check = False
                break
                
        if check:
            answer.append(n)
    
    print(list(set(answer)))
    
    return len(set(answer))

numbers = "011"
print(solution(numbers)) # 2