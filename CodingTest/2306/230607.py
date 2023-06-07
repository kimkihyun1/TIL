'''
    프로그래머스 : 피보나치 수
'''

def solution(n):
    fin = [0, 1]
    for i in range(2, n+1):
        fin.append(fin[i-2] + fin[i-1])
        
    return fin[n] % 1234567

n = 5
print(solution(n))
# 5