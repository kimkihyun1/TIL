'''
    프로그래머스 : 사칙연산
    https://school.programmers.co.kr/learn/courses/30/lessons/1843
'''

def solution(arr):
    nums = [int(x) for x in arr[::2]]
    ops = [x for x in arr[1::2]]
    
    maxs = {}
    mins = {}
    
    for i in range(len(nums)):
        maxs[(i, i)] = nums[i]
        mins[(i, i)] = nums[i]
        
        # print(maxs, mins) 
        # {(0, 0): 1, (1, 1): 3, (2, 2): 5, (3, 3): 8} {(0, 0): 1, (1, 1): 3, (2, 2): 5, (3, 3): 8}
        
    for d in range(1, len(nums)):
        for i in range(len(nums)):
            j = i + d
            if j >= len(nums):
                continue
            
            max_nums, min_nums = [], []
            
            for k in range(i+1, j+1):
                if ops[k-1] == '-':
                    mx = maxs[(i, k-1)] - mins[(k, j)]
                    mn = mins[(i, k-1)] - maxs[(k, j)]
                    max_nums.append(mx)
                    min_nums.append(mn)
                else:
                    mx = maxs[(i, k-1)] + maxs[(k, j)]
                    mn = mins[(i, k-1)] + mins[(k, j)]
                    max_nums.append(mx)
                    min_nums.append(mn)
                    
                # print(max_nums, min_nums)
                # [-2] [-2]
                # [8] [8]        
                # [-3] [-3]      
                # [-7] [-7]      
                # [-7, 3] [-7, 3]
                # [0] [0]        
                # [0, 0] [0, 0]  
                # [1] [1]
                # [1, -5] [1, -5]
                # [1, -5, -5] [1, -5, -15]
                    
            maxs[(i, j)] = max(max_nums)
            mins[(i, j)] = min(min_nums)
            
            # print(maxs)
            # {(0, 0): 1, (1, 1): 3, (2, 2): 5, (3, 3): 8, (0, 1): -2, (1, 2): 8, (2, 3): -3, (0, 2): 3, (1, 3): 0, (0, 3): 1} 
            # print(mins)
            # {(0, 0): 1, (1, 1): 3, (2, 2): 5, (3, 3): 8, (0, 1): -2, (1, 2): 8, (2, 3): -3, (0, 2): -7, (1, 3): 0, (0, 3): -15}
                   
    return maxs[(0, len(nums)-1)]

arr = ["1", "-", "3", "+", "5", "-", "8"]
print(solution(arr)) # 1