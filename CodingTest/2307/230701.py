'''
    프로그래머스 : 스킬트리
'''

def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skill_list = list(skill)
        
        for i in skill_tree:
            if i in skill:
                if i != skill_list.pop(0):
                    break
                    
        else:
            answer += 1
    
    
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))
# 2