'''
    프로그래머스 : 순위 검색 (카카오)
    Lower Bound : 원하는 값 이상이 처음 나오는 위치를 찾는 과정
    bisect 라이브러리의 bisect_left 함수 사용
'''

from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    dic = defaultdict(list)
    for info_ in info:
        info_ = info_.split()
        condition = info_[:-1]
        score = int(info_[-1])
        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = '-'
                key = ''.join(tmp)
                dic[key].append(score)
                
    for value in dic.values():
        value.sort()
    
    for query_ in query:
        query_ = query_.replace('and ', '')
        query_ = query_.split()
        target_key = ''.join(query_[:-1])
        target_score = int(query_[-1])
        count = 0
        if target_key in dic:
            target_list = dic[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)
        
    return answer