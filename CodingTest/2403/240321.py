'''
    프로그래머스 : 개인정보 수집 유효기간(카카오)
    https://school.programmers.co.kr/tryouts/85964/challenges?language=python3
'''

def days(date):
    year, month, day = map(int, date.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    months = {t[0]: int(t[2:]) * 28 for t in terms}
    today = days(today)
    answer = [i + 1 for i, p in enumerate(privacies)
             if days(p[:-2]) + months[p[-1]] <= today]
    
    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today, terms, privacies))