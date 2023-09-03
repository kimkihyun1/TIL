'''
    프로그래머스 : 가위 바위 보
    https://school.programmers.co.kr/tryouts/85898/challenges?language=python3
'''

def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '2':
            answer += '0'
        elif i == '0':
            answer += '5'
        else:
            answer += '2'
    return answer

rsp = "205"
print(solution(rsp))
# '052'