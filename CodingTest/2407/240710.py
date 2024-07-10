'''
    프로그래머스 : 단어 변환
    https://school.programmers.co.kr/learn/courses/30/lessons/43163
'''

from collections import deque

def solution(begin, target, words):
  
    if target not in words:
        return 0
    
    queue = deque()
    queue.append([begin, 0])
    
    while queue:
        pop_word, num = queue.popleft()
        
        if pop_word == target:
            return num
        
        for word in words:
            count = 0
            for i in range(len(word)):
                # 알파벳이 다르면 +1
                if pop_word[i] != word[i]:
                    count += 1
            
            # 하나의 알파벳만 바뀌면
            if count == 1:
                queue.append([word, num+1])

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words)) # 4