'''
    프로그래머스 : 등굣길
    https://school.programmers.co.kr/tryouts/85953/challenges
'''

def solution(m, n, puddles):
    answer = 0
    puddles = [[j, i] for [i, j] in puddles]
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    for m in range(1, m+1):
        for n in range(1, n+1):
            if m == 1 and n == 1:
                continue
            elif [n, m] in puddles:
                dp[n][m] = 0
            else:
                dp[n][m] = (dp[n-1][m] + dp[n][m-1]) % 1000000007
    
    answer = dp[n][m]
    
    return answer

m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))