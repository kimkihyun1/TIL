'''
    프로그래머스 : 문자열 다루기 기본
'''

def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():     # isdigit() : 문자열이 숫자로만 이루어져 있는지 확인
            return True
        else:
            return False
    else:
        return False
    
s = "a234"
#s = "1234"
print(solution(s))