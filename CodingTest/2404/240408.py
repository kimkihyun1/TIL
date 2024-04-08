'''
    프로그래머스 : 타겟 넘버
    https://school.programmers.co.kr/learn/courses/30/lessons/43165
'''
def solution(numbers, target):
    answer = 0
    stack = [[numbers[0], 0], [-1*numbers[0], 0]]
    len_num = len(numbers)
    
    while stack:
        tmp, idx = stack.pop()
        idx += 1
        
        if idx < len_num:
            stack.append([tmp + numbers[idx], idx])
            stack.append([tmp - numbers[idx], idx])
        else:
            if tmp == target:
                answer += 1
    
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target)) # 5 