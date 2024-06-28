'''
    프로그래머스 : 카펫
    https://school.programmers.co.kr/learn/courses/30/lessons/42842
'''

def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow % i == 0:
            y_row = int(yellow/i)
            y_col = i
            if (2*(y_row+y_col)+4 == brown):
                return [y_row+2, y_col+2]
            
brown = 10
yellow = 2
print(solution(brown, yellow)) # [4, 3]