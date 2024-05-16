'''
    프로그래머스 : 모의고사
    https://school.programmers.co.kr/learn/courses/30/lessons/42840
'''

def solution(answers):
    answer = [0, 0, 0]
    result = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i, ans in enumerate(answers):
        if ans == p1[i % len(p1)]:
            answer[0] += 1
        if ans == p2[i % len(p2)]:
            answer[1] += 1
        if ans == p3[i % len(p3)]:
            answer[2] += 1
    
    for i, cnt in enumerate(answer):
        if cnt == max(answer):
            result.append(i + 1)
        
    return result

answers = [1, 3, 2, 4, 2]
print(solution(answers)) # [1, 2, 3]