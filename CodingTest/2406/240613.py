'''
    프로그래머스 : 등굣길
    https://school.programmers.co.kr/learn/courses/30/lessons/42898?language=python3
'''

def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    for i, j in puddles:
        dp[j][i] = -1
        
    for i in range(1, m+1):
        for j in range(1, n+1):
            if dp[j][i] == -1:
                dp[j][i] = 0
                continue
        
            dp[j][i] += (dp[j-1][i] + dp[j][i-1]) % 1000000007
    
    return dp[n][m]

m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles)) # 4