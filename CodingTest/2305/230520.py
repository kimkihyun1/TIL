'''
    프로그래머스 : 카펫
'''

def solution(brown, yellow):
    for i in range(1, yellow+1):
        if yellow % i == 0:
            yellow_row = yellow // i
            yellow_col = i
            if 2 * (yellow_row + yellow_col) + 4 == brown:
                return [yellow_row + 2, yellow_col + 2]
            
brown = 10
yellow = 2
print(solution(brown, yellow))
# [4, 3]