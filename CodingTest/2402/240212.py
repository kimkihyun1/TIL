'''
    프로그래머스 : 가까운 수
    https://school.programmers.co.kr/tryouts/85945/challenges?language=python3
'''

def solution(array, n):
    answer = 0
    num = []
    
    # 가장 가까운 거리가 여러 개일 때를 대비해 미리 정렬하여 바로 답을 찾게한다. 
    array.sort() 
    
    for i in array:
        num.append(abs(n-i))

    answer = array[num.index(min(num))]
    
    return answer
    
array = [3, 10, 28, 12]
n = 20
print(solution(array, n)) # 12