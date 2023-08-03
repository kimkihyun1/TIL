'''
    프로그래머스 : 외톨이 알파벳(PCCP)
    https://school.programmers.co.kr/tryouts/72136/challenges?language=python3
'''

def solution(input_string):
    answer = ''
    alpha_dict = {}
    answer_list = []
    
    for idx, alpha in enumerate(input_string):
        if alpha not in alpha_dict:
            alpha_dict[alpha] = [idx]
        else:
            alpha_dict[alpha].append(idx)
            
    for k, v in alpha_dict.items():
        if len(v) >= 2:
            for i in range(len(v) - 1):
                if abs(v[i] - v[i + 1]) > 1:
                    answer_list.append(k)
                    break
                
    if len(answer_list) == 0:
        answer = 'N'
    else:
        answer = ''.join(sorted(answer_list))
        
    return answer

input_string = "edeaaabbccd"
print(solution(input_string))
# 'de'