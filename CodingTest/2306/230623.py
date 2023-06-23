'''
    프로그래머스 : 보석 쇼핑(카카오)
'''

def solution(gems):
    answer = [0, len(gems)]
    size = len(set(gems))  # 보석 종류 개수
    left, right = 0, 0
    gem_dict = {gems[0] : 1}
    
    while left < len(gems) and right < len(gems):
        if len(gem_dict) == size:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            else:
                gem_dict[gems[left]] -= 1
                if gem_dict[gems[left]] == 0:
                    del gem_dict[gems[left]]
                left += 1
            
        else:
            right += 1
            
            if right == len(gems):
                break
            
            gem_dict[gems[right]] = gem_dict.get(gems[right], 0) + 1
    
    return [answer[0]+1, answer[1]+1]

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))
# [3, 7]