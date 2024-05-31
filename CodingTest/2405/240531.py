'''
    프로그래머스 : 전화번호 목록
    https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3
'''

def solution(phone_book):
    answer = True
    hash_map = {}
    
    for number in phone_book:
        hash_map[number] = 1
    
    print(hash_map) # {'119': 1, '97674223': 1, '1195524421': 1}
    
    for number in phone_book:
        num_arr = ""
        
        for num in number:
            num_arr += num
            
            # hash_map안의 번호와 일치하고 본인의 번호을 제외
            if num_arr in hash_map and num_arr != number:
                answer = False
        
    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book)) # False