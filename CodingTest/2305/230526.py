'''
    프로그래머스 : 문자열 내 마음대로 정렬하기
'''

def solution(strings, n):
    
    return sorted(strings, key=lambda x:(x[n], x)) # 튜플로 정렬의 우선순위를 정함