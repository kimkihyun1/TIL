'''
    프로그래머스 : 프로세스
    https://school.programmers.co.kr/learn/courses/30/lessons/42587
'''

def solution(priorities, location):
    answer = 0
    queue = [(idx, prior) for idx, prior in enumerate(priorities)]
    #print(queue)  [(0, 2), (1, 1), (2, 3), (3, 2)]
    
    while True:
        first = queue.pop(0)
        # any() : 하나라도 True이면 True
        if any(first[1] < q[1] for q in queue): 
            queue.append(first)
        else:
            answer += 1 
            if first[0] == location:
                return answer
        
priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location)) # 1
