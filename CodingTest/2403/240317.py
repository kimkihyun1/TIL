'''
    프로그래머스 : 키패드 누르기(카카오)
    https://school.programmers.co.kr/tryouts/85961/challenges?language=python3
'''

def solution(numbers, hand):
    answer = ''
    
    # 각 숫자들의 좌표
    left = {1: 3, 4: 2, 7: 1}
    center = {2: 3, 5: 2, 8: 1, 0: 0}
    right = {3: 3, 6: 2, 9: 1}
    
    # 시작 좌표 설정
    left_hand = (0, 0)
    right_hand = (2, 0)
    
    for num in numbers:
        if num in left:
            answer += 'L'
            left_hand = (0, left[num])
        elif num in right:
            answer += 'R'
            right_hand = (2, right[num])
        # 가운데 숫자일 시
        else:
            # 현재 손의 좌표와 숫자의 거리 계산
            left_dist = 1 - left_hand[0] + abs(left_hand[1] - center[num])
            right_dist = right_hand[0] - 1 + abs(right_hand[1] - center[num])
            
            if left_dist < right_dist:
                answer += 'L'
                left_hand = (1, center[num])
            elif left_dist > right_dist:
                answer += 'R'
                right_hand = (1, center[num])
            else:
                if hand == 'left':
                    answer += 'L'
                    left_hand = (1, center[num])
                elif hand == 'right':
                    answer += 'R'
                    right_hand = (1, center[num])
            
    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand)) # "LRLLLRLLRRL"