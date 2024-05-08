'''
    프로그래머스 : 기능개발
    https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3
'''

def solution(progresses, speeds):
    answer = []
    count = 0
    time = 0
    
    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds)) # [2, 1]