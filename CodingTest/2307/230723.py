'''
    프로그래머스 : 신고 결과 받기(카카오)
'''

from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report = list(set(report)) # 중복 제거
    user = defaultdict(set) 
    count = defaultdict(int)
    
    for r in report:
        a, b = r.split() 
        user[a].add(b) # 신고자가 신고한 id 추가
        count[b] += 1 
        
    for id in id_list:
        mail = 0 # 받은 메일수
        for u in user[id]:
            if count[u] >= k:
                mail += 1  
        answer.append(mail)
        
    return answer    

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))