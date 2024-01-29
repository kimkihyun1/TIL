'''
    프로그래머스 : 콜라츠 추측
    https://school.programmers.co.kr/tryouts/85936/challenges?language=python3
'''

def solution(num):
    answer = 0
    
    while True:
        if num == 1:
            break
        if answer == 500:
            return -1
        if num % 2 == 0:
            num /= 2
            answer += 1
        else:
            num = num * 3 + 1
            answer += 1          
            
    return answer

num = 6
print(solution(num)) # 8