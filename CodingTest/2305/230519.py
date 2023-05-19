'''
    프로그래머스 : 모의고사
'''
def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2 ,1 ,2 ,3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    answer = []
    
    for idx, ans in enumerate(answers):
        if ans == student1[idx % len(student1)]:
            score[0] += 1
        if ans == student2[idx % len(student2)]:
            score[1] += 1
        if ans == student3[idx % len(student3)]:
            score[2] += 1
    
    for idx, num in enumerate(score):
        if num == max(score):
            answer.append(idx+1)
            
    return answer    

answers = [1,2,3,4,5]
print(solution(answers))
# 1