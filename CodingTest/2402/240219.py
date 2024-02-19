'''
    프로그래머스 : N으로 표현
    https://school.programmers.co.kr/tryouts/85952/challenges?language=python3
'''

def solution(N, number):
    # 집합을 저장할 리스트
    dp = [set() for _ in range(9)]
    
    # N 초기화
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        
    # 연산
    for i in range(1, 9):
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i - j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
                        
        if number in dp[i]:
            return i
    
    return -1

N = 5
number = 12
print(solution(N, number)) # 4