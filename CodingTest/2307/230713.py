'''
    프로그래머스 : 단어 변환
'''

from collections import deque

def change(word, ch_word, begin):
        diff = 0
        for i in range(len(begin)):
            if word[i] != ch_word[i]:
                diff += 1
        if diff == 1:
            return True
        else:
            return False

def bfs(begin, target, words):
        queue.append([begin, 0])
        
        if target not in words:
            return 0

        while queue:
            word, count = queue.popleft()
            for ch_word in words:
                if change(word, ch_word, begin):
                    if ch_word == target:
                        return count + 1
                    else:
                        queue.append([ch_word, count+1])

def solution(begin, target, words):
    global queue
    queue = deque()  
    answer = bfs(begin, target, words)
    
    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))
# 4