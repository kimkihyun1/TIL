'''
    프로그래머스 : 호텔 방 배정
'''

import sys
sys.setrecursionlimit(10000) # 재귀 허용깊이

def solution(k, room_number):
    rooms = dict() # {방번호 : 다음 빈방 번호}
    for num in room_number:
        check_in = emptyroom(num, rooms)
    
    return list(rooms.keys())

def emptyroom(check, rooms): 
    if check not in rooms.keys(): # 빈 방일시
        rooms[check] = check + 1
        return check
    empty = emptyroom(rooms[check], rooms)
    rooms[check] = empty + 1
    return empty

k = 10
room_number = [1,3,4,1,3,1]
print (solution(k, room_number))
# [1,3,4,2,5,6]
        