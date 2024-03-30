'''
    프로그래머스 : 폰켓몬
    https://school.programmers.co.kr/learn/courses/30/lessons/1845
'''

def solution(nums):
    len_nums = len(nums) // 2
    
    if len_nums > len(set(nums)): # set() : 중복을 제거
        return len(set(nums))
    
    return len_nums

nums = [3,1,2,3]
print(solution(nums)) # 2