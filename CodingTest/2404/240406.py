'''
    프로그래머스 : N으로 표현
    https://school.programmers.co.kr/learn/courses/30/lessons/42895
'''

def solution(N, number):
    # [{5}, {55}, {555}, {5555}, {55555}, {555555}, {5555555}, {55555555}]
    dp = [set([int(str(N)*i)])for i in range(1, 9)]
    
    # 최솟값 8 이하만 연산
    for i in range(8):
        for j in range(i):
            for num1 in dp[j]:
                for num2 in dp[i-j-1]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)
        
        if number in dp[i]:
            return i + 1
    
    # 최솟값이 8보다 크면 -1
    return -1

N = 5
number = 12
print(solution(N, number)) # 4