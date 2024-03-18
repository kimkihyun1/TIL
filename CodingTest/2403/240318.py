'''
    프로그래머스 : 대충 만든 자판
    https://school.programmers.co.kr/tryouts/85962/challenges?language=python3
'''

def solution(keymap, targets):
    answer = []
    
    for target in targets:
        count = []
        
        for char in target:
            index = []
            
            for key in keymap:
                if char in key:
                    # key의 인덱스 자리수를 찾는다
                    index.append(key.find(char))
            
            if index:
                # 각 key 인덱스 자리수가 제일 낮은 수 추가
                count.append(min(index))
        
        # index는 0으로 시작하므로 1씩 더해주어야한다.
        answer.append(sum(count) + len(count) if len(count) == len(target) else -1)
        
    return answer

keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]
print(solution(keymap, targets)) # [9, 4]