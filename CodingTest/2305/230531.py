'''
    프로그래머스 : 징검다리 건너기
'''

def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for st in stones:
            if st - mid <= 0:
                count += 1
            else:
                count = 0
            if count >= k:
                break
        if count >= k:
            right = mid - 1
        else:
            left = mid + 1
            
    return left

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))
# 3