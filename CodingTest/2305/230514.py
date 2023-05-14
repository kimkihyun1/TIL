'''
    프로그래머스 : 휴대폰 번호 가리기
'''
def solution(phone_number):
    answer = '*' * (len(phone_number) - 4) + phone_number[-4:]
    
    return answer

phone_number = "01033334444"
print(solution(phone_number))
# "*******4444"