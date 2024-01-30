'''
    프로그래머스 : 여행 경로
    https://school.programmers.co.kr/tryouts/85937/challenges?language=python3
'''

from collections import defaultdict

def solution(tickets):
    answer = []
    path = ['ICN']
    
    # 딕셔너리 생성
    tickets_dict = defaultdict(list)
    for start, end in tickets:
        tickets_dict[start].append(end)
    
    # 내림차순 정렬
    for ticket_key in tickets_dict.keys():
        tickets_dict[ticket_key].sort(reverse=True)
        
    # 로직
    while path:
        now = path[-1]
        if now not in tickets_dict or len(tickets_dict[now]) == 0:
            answer.append(path.pop())
        else:
            path.append(tickets_dict[now].pop())
    
    return answer[::-1]

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets)) # ["ICN", "JFK", "HND", "IAD"]
