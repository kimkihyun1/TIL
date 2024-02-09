'''
    프로그래머스 : 숫자 짝꿍
    https://school.programmers.co.kr/tryouts/85942/challenges?language=python3
'''

def solution(X, Y):
    answer = ''
    
    # 내림차순으로 카운트하여 바로 가장 큰 수가 나오게 정렬
    for i in range(9, -1, -1):
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))
    
    if answer == "":
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    
    return answer

X = "12321"
Y = "42531"
print(solution(X, Y)) # "321"