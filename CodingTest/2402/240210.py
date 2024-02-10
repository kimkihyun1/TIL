'''
    프로그래머스 : A로 B 만들기
    https://school.programmers.co.kr/tryouts/85943/challenges?language=python3
'''

def solution(before, after):
    answer = 0
    cnt = 0
    
    for i in before:
        if before.count(str(i)) == after.count(str(i)):
            cnt += 1
    
    if len(before) == cnt:
        answer = 1
    
    return answer

before = "allpe"
after = "apple"
print(solution(before, after)) # 0