'''
    프로그래머스 : 체육대회(PCCP)
    https://school.programmers.co.kr/tryouts/72137/challenges?language=python3
'''

answer = 0

def dfs(people, sum, ability, check):
    global answer
    student = len(ability)
    play = len(ability[0])
    
    if people == play:
        answer = max(answer, sum)
    else:
        for i in range(student):
            if check[i] == 0:
                check[i] = 1
                dfs(people+1, sum + ability[i][people], ability, check)
                check[i] = 0

def solution(ability):
    global answer 
    check = [0] * len(ability) # 학생 배열
    dfs(0, 0, ability, check)
    
    return answer

ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
print(solution(ability))
# 210