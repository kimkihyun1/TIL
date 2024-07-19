'''
    프로그래머스 : 도둑질
    https://school.programmers.co.kr/learn/courses/30/lessons/42897
'''

def solution(money):
    dp_firsthome = [0] * len(money)
    dp_lasthome = [0] * len(money)
    
    # 첫번째 집을 포함, 마지막 집 포함X
    dp_firsthome[0] = money[0]
    for i in range(1, len(money)-1):
        dp_firsthome[i] = max(dp_firsthome[i-1], dp_firsthome[i-2] + money[i])
    
    print(dp_firsthome) # [1, 2, 4, 0]
    
    # 첫번째 집을 포함X, 마지막 집 포함
    for i in range(1, len(money)):
        dp_lasthome[i] = max(dp_lasthome[i-1], dp_lasthome[i-2] + money[i])
    
    print(dp_lasthome) # [0, 2, 3, 3]
    
    answer = max(dp_firsthome[-2], dp_lasthome[-1])
    
    return answer

money = [1, 2, 3, 1]
print(solution(money)) # 4