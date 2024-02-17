'''
    프로그래머스 : 체육복
    https://school.programmers.co.kr/tryouts/85950/challenges?language=python3
'''

def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    
    # reserve[:]를 사용 이유 : reserve 리스트의 복사본을 만들어 반복하고 
    # 리스트에 대한 반복 동안 수정이 일어나도 루프에 영향을 주지 않다.
    for i in reserve[:]:  
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
    
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
            
    answer = n - len(lost)
    
    return answer

n = 5
lost = [2, 4]
reserve = [1, 3, 5]
print(solution(n, lost, reserve)) # 5