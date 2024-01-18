'''
    프로그래머스 : 기능 개발
    https://school.programmers.co.kr/tryouts/85931/challenges
'''

def solution(progresses, speeds):
    answer = []
    day = 0
    cnt = 0
    
    while len(progresses) > 0:
        if (progresses[0] + day * speeds[0]) >= 100: # 작업이 100% 될 시
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            else:
                day += 1
    
    answer.append(cnt) # 마지막 작업
    
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds)) # [2, 1]