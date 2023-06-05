'''
    프로그래머스 : 오픈채팅방
'''

def solution(record):
    answer = []
    dic = {}
    for rec in record:
        rec = rec.split()
        if len(rec) == 3:
            dic[rec[1]] = rec[2]
            
    for rec in record:
        rec = rec.split()
        if rec[0] == "Enter":
            answer.append("%s님이 들어왔습니다." % dic[rec[1]])
        elif rec[0] == "Leave":
            answer.append("%s님이 나갔습니다." % dic[rec[1]])
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
