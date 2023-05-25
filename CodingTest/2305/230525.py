'''
    프로그래머스 : H-index
'''

def solution(citations):
    citations.sort()
    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx:
            return len(citations) - idx
        
    return 0

citations = [3, 0, 6, 1, 5]
print(solution(citations))
# 3