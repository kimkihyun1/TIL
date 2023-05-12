'''
    프로그래머스: 이진 변환 반복하기
    
'''

def solution(s):
    cnt = 0
    cnt_zero = 0
    
    while s != '1':
        cnt_zero += s.count('0')  # 0의 수를 카운트 
        s = s.replace('0', '')    # '0'을 지운다
        s = bin(len(s))[2:]       # bin 함수는 십진수를 이진수로 나타낸다
        cnt += 1                  # [2:]를 한 이유는 bin함수는 앞에 0b를 앞에 붙이기 때문에 제거하기 위해서이다
    
    answer = [cnt, cnt_zero]
    return answer

s = "110010101001"
print(solution(s))