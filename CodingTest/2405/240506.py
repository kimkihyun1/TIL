'''
    프로그래머스 : 완주하지 못한 선수
    https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3
'''

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer += ''.join(participant[i])
            return answer
        
    answer += ''.join(participant[-1])
    
    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion)) # "leo"