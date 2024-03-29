'''
    프로그래머스 : 표현 가능한 이진트리
    https://school.programmers.co.kr/tryouts/85967/challenges?language=python3
'''

from math import log2

def solution(numbers):
    answer = []
    
    for num in numbers:
        bin_num = bin(num)[2:] # 2진수로 변환
        bin_len = len(bin_num)
        
        # 1, 3, 7, ...
        node_count = 2 ** (int(log2(bin_len)) + 1) - 1
        bin_num = "0" * (node_count - bin_len) + bin_num
        
        # num = 5 이면 bin_num = 101
        # 루트 노드가 더미 노드일 수 없다
        if bin_num[node_count // 2] == "0":
            answer.append(0)
            continue
        
        # 가능, 불가능 구분
        is_possible = 1
        # 가장 왼쪽, 가장 오른쪽
        stack = [[0, node_count - 1]]
        
        # DFS
        while stack:
            left, right = stack.pop()
            
            if left == right:
                continue
            
            center = (left + right) // 2
            
            # 서브트리 존재할 경우, 루트 노드가 0이면 진행 불가
            if bin_num[center] == "0" and "1" in bin_num[left:right+1]:
                is_possible = 0
                break
            
            # 서브트리를 2개로 분할
            stack.extend([[left, center-1], [center+1, right]])
            
        answer.append(is_possible)
        
    return answer    


numbers = [7, 42, 5]
print(solution(numbers)) # [1, 1, 0]