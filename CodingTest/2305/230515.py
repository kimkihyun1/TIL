'''
    프로그래머스 : 콜라츠 추측
    반목문과 재귀함수를 둘 다 사용하여 
    시간을 측정해 본 결과
    반복문이 더 빠르다는 것이 확인된다.
'''
import math
import time

# while문 사용
def solution(num):   
    count = 0
    if num == 1:
        return 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        count += 1
        if count == 500:
            return -1
    return count

# 재귀함수 사용
def recursion(num):
    count = 0
    def recur(n):
        nonlocal count
        if n == 1:
            return count
        elif count == 500:
            return -1
        elif n % 2 == 0:
            count += 1
            return recur(n/2)
            
        else:
            count += 1
            return recur(n*3+1)
    
    return recur(num)

num = 626331

start = time.time()
print(solution(num))  # -1
end = time.time()
print('반복문: ', end - start)

start = time.time()
print(recursion(num)) # -1
end = time.time()
print('재귀 : ', end - start)