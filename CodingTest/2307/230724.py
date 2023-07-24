'''
    프로그래머스 : k진수에서 소수 개수 구하기(카카오)
'''

def solution(n, k):
    num = ''
    while n:
        num = str(n%k) + num   # 진법 변환
        n //= k
    
    num = num.split('0')
    count = 0
    
    for i in num:
        if len(i) == 0:
            continue
        if int(i) < 2:
            continue
        flag = True
        for j in range(2, int(int(i)**0.5)+1): # 소수 찾기
            if int(i) % j == 0:
                flag = False
                break
        if flag:
            count += 1
            
    return count     

n = 437674
k = 3
print(solution(n, k))
# 3