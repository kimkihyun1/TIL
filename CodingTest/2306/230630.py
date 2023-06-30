'''
    프로그래머스 : 2개 이하로 다른 비트
'''

def solution(numbers):
    answer = []
    for number in numbers:
        bin_num = list('0' + bin(number)[2:])
        idx = ''.join(bin_num).rfind('0')   # rfind : 오른쪽에서부터 찾는다
        bin_num[idx] = '1'
        
        if number % 2 == 1:   # 홀수 일때
            bin_num[idx+1] = '0'  # 1로 바꾼 자리의 바로 뒤를 0으로 바꾸어준다.
        
        answer.append(int(''.join(bin_num), 2))   # int(num, 2) : num을 2진수에서 10진수로 바꾸어준다.
    return answer

numbers = [2,7]
print(solution(numbers))
# [3, 11]