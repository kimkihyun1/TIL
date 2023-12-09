'''
    프로그래머스 : 최빈값 구하기
'''

def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0:
            return a
    return -1

array = [1, 2, 3, 3, 3, 4]
print(solution(array)) # 3