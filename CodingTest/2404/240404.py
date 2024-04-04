'''
    프로그래머스 : 최소직사각형
    https://school.programmers.co.kr/learn/courses/30/lessons/86491
'''

def solution(sizes):
    w = []
    h = []
    
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]: # 둘 중 큰 값을 w 리스트에 추가
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0]) 
            w.append(sizes[i][1])
            
    return max(w) * max(h)

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes)) # 4000