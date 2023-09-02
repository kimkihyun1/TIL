'''
    프로그래머스 : 옹알이(2)
    https://school.programmers.co.kr/tryouts/85897/challenges?language=python3
'''

def solution(babbling):
    answer = 0
    babble = ['aya', 'ye', 'woo', 'ma']
    for word in babbling:
        print(word)
        for b in babble:
            print(b)
            if b * 2 not in word:
                word = word.replace(b, ' ')
                print(word)
                print()
        if word.strip() == '':
            answer += 1
            
    return answer

babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babbling))
# 2