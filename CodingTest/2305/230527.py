'''
    프로그래머스 : 가장 큰 수
    
'''

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    '''
        x*3을 한 이유는 [3, 30, 34, 5, 9] 배열을 그냥 정렬하게 되면 
        [9,5,34,30,3] 으로 정렬된다 3이 30보다 앞에 있어야 한다.
        number 수는 1000이하 이므로 최대값을 생각하면
        [999, 555, 343434, 303030, 333] 으로 이것을 정렬하면 
        [999, 555, 343434, 333, 303030]이 된다.
    '''
    print(numbers)
    
    return str(int(''.join(numbers)))

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))
