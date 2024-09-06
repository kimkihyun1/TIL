'''
    프로그래머스 : 주식가격
    https://school.programmers.co.kr/learn/courses/30/lessons/42584?language=python3
'''

def solution(prices): 
    n = len(prices)
    answer = [0] * n  # 각 주식이 몇 번 유지되는지 기록할 리스트
    stack = []

    for i in range(n):
        # 스택이 비어있지 않고 현재 가격이 스택의 최상단 가격보다 낮다면
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j  # 가격이 떨어진 시점을 기록
        stack.append(i)
        
    # 끝까지 가격이 떨어지지 않은 경우 처리
    while stack:
        j = stack.pop()
        answer[j] = n - j - 1  # 끝까지 유지된 시간을 계산
        
    return answer

prices = [1, 2, 3, 2, 3]	
print(solution(prices)) # [4, 3, 1, 1, 0]
