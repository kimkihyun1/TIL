'''
    프로그래머스 : 신규 아이디 추천
'''

def solution(new_id):
    answer = ''
    new_id = new_id.lower() #소문자로 변환
    for word in new_id:
        if word.isalnum() or word in '-_.':  # isalnum() : 문자열이 한글,영어,숫자 되어있으면 참 리턴
            answer += word
    
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    else:
        answer = answer
    
    if answer[-1] == '.':
        answer = answer[:-1]
    else:
        answer = answer
        
    if answer == '':
        answer = 'a'
    
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
            
    if len(answer) < 3:
        answer = answer + answer[-1] * (3-len(answer))
        
    return answer 

new_id = "...!@BaT#*..y.abcdefghijklm"

print(solution(new_id)) 
# "bat.y.abcdefghi"