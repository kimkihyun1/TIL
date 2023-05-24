'''
    프로그래머스 : 두 개 뽑아서 더하기
'''

from itertools import combinations

def solution(numbers):
    answer = set()
    for i in list(combinations(numbers, 2)):
        answer.add(sum(i))
    
    answer = list(answer)    # set 을 정렬하기 위해 list로 변환
    answer.sort()
    
    return answer

numbers = [2,1,3,4,1]
print(solution(numbers))
# [2,3,4,5,6,7]