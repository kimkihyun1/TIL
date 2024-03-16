'''
    프로그래머스 : 기사단원의 무기
    https://school.programmers.co.kr/tryouts/85960/challenges?language=python3
'''

def solution(number, limit, power):
    answer = 0
    
    for num in range(1, number+1):
        cnt = 0
        # 수를 1/2로 나누어 계산
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                # 같은 수를 곱해서 해당 수가 나오면 약수가 1개이므로 1 증가
                if i * i == num:
                    cnt += 1
                # 아닐 시 약수가 2개이므로 2 증가
                else:
                    cnt += 2
        
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    
    return answer

number = 5
limit = 3
power = 2
print(solution(number, limit, power)) #  10