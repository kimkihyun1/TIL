'''
    프로그래머스 : 프로세스
    https://school.programmers.co.kr/tryouts/85932/challenges?language=python3
'''

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
            
priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location)) # 1