def solution(n):
    answer = hanoi(n, 1, 3, 2)
    return answer

def hanoi(n, start, end, mid):
    if n == 1:
        return [[start, end]]
    else:
        answer =[]
        answer += hanoi(n-1, start, mid, end)
        answer += [[start, end]]
        answer += hanoi(n-1, mid, end, start)
        
        return answer
    
print(solution(2))
# [ [1,2], [1,3], [2,3] ]