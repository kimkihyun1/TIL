'''
    프로그래머스 : 완주하지 못한 선수
'''

def solution(participant, completion):
    hashdic= {}
    hashsum = 0
    
    for part in participant:
        hashdic[hash(part)] = part
        hashsum += hash(part)
        
    for comp in completion:
        hashsum -= hash(comp)
        
    return hashdic[hashsum]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))
# mislav