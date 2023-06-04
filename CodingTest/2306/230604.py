'''
    프로그래머스 : 위장
'''

def solution(clothes):
    hash_map = {}
    for cloth, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1   # 종류별로 구분
        # get() : 첫번째 인자는 찾고자 하는 키를 넣고 두번째 인자는 키가 없을 시 넣을 값을 적는다.
        
    answer = 1
    for type in hash_map:
        answer *= (hash_map[type] + 1)  # 입지 않은 경우까지 추가하여 계산
    
    return answer - 1   # 아무것도 입지 않은 경우는 제외시킨다.

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))