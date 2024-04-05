'''
    프로그래머스 : 체육복
    https://school.programmers.co.kr/learn/courses/30/lessons/42862?language=python3
'''

def solution(n, lost, reserve):
    lost_reserve = set(reserve) & set(lost) # 도난 당했지만 여별의 체육복을 가진 학생
    lost_clothes = set(lost) - lost_reserve # 도난당한 학생
    reserve_clothes = set(reserve) - lost_reserve # 여벌옷을 가진 학생
    # set() 자료형으로 리스트의 중복을 제거하고 정렬할 수 있다.
    
    for i in reserve_clothes:
        if i - 1 in lost_clothes:
            lost_clothes.remove(i-1)
        elif i + 1 in lost_clothes:
            lost_clothes.remove(i+1)
    
    return n - len(lost_clothes)

n = 5
lost =	[2, 3, 4]
reserve = [5, 3, 1]
print(solution(n, lost, reserve)) # 5