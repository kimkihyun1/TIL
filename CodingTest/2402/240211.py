'''
    프로그래머스 : 등수 매기기
    https://school.programmers.co.kr/tryouts/85944/challenges?language=python3
'''

def solution(score):
    answer = []
    avg = []
    
    for i in range(len(score)):
        avg.append(sum(score[i]) / 2) 
    
    avg_sort = sorted(avg, reverse=True) # sorted() : 내장함수로써, 리스트의 원본 값은 그대로이고 정렬 값을 반환
    
    for i in avg:
        answer.append(avg_sort.index(i) + 1)
    
    return answer

score = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
print(solution(score)) # [4, 4, 6, 2, 2, 1, 7]