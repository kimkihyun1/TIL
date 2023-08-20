'''
    프로그래머스 : 옹알이 (1)
    https://school.programmers.co.kr/tryouts/85889/challenges?language=python3
'''

def solution(babbling):
    answer = 0
    
    for w in babbling:
        count = 0
        word = ''
        for i in w:
            word += i
            if word in ['aya', 'ye', 'woo', 'ma']:
                word = ''
                count += 1
        if len(word) == 0 and count > 0:
            answer += 1
            
    return answer

babbling = ["aya", "yee", "u", "maa", "wyeoo"]
print(solution(babbling))
# 1