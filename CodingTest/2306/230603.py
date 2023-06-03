'''
    프로그래머스 : 전화번호 목록
    
    zip 함수
    print(list(zip([1,2,3], (4,5,6), "abcd")))
    [[1, 4, 'a'], [2, 5, 'b'], [3, 6, 'c']]
    
    startswith
    print("dfagd".startswith("abcd"))  False
    print("abcde".startswith("abcd"))  True

'''

def solution(phone_book):
    phone_book = sorted(phone_book)
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    
    return True
        
phone_book = ["119", "97674223", "1195524421"]   
print(solution(phone_book))
# False    