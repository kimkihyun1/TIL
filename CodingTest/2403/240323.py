'''
    프로그래머스 : 이모티콘 할인행사(카카오)
    https://school.programmers.co.kr/tryouts/85965/challenges?language=python3
'''

def solution(users, emoticons):
    def loop(counts):
        # counts : 할인하지 않는 이모티콘 수
        if counts == 0:
            plus = 0
            total = 0
            for user in users:
                revenue = 0
                for i, em in enumerate(temp):
                    # 이모티콘의 할인율이 사용자 할인율보다 높을 때
                    if em * 10 >= user[0]:
                        revenue += (emoticons[i] // 10) * (10 - em)
                if revenue >= user[1]:
                    plus += 1
                else:
                    total += revenue
            
            # 플러스 가입자를 늘리는 것이 우선순위
            if plus > answer[0] or (plus == answer[0] and total > answer[1]):
                answer[0], answer[1] = plus, total
            
            return
        
        for i in range(1, 5):
            # 할인율 10 ~ 40%을 temp의 뒤에서부터 지정
            temp[counts - 1] = i
            loop(counts - 1)


    temp = [-1] * len(emoticons)
    answer = [0, 0]
    loop(len(emoticons))

    return answer

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
print(solution(users, emoticons)) 