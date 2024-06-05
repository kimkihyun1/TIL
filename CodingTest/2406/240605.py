'''
    프로그래머스 : H-Index
    https://school.programmers.co.kr/learn/courses/30/lessons/42747
'''

def solution(citations):
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i
    
    return len(citations)

citations = [3, 0, 6, 1, 5]
print(solution(citations)) # 3