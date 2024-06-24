'''
'''

def solution(clothes):
    answer = 1
    cloth = {}
    
    for name, kind in clothes:
        if kind in cloth.keys():
            cloth[kind] += [name]
        else:
            cloth[kind] = [name]
            
    print(cloth) # {'headgear': ['yellow_hat', 'green_turban'], 'eyewear': ['blue_sunglasses']}
    
    for _, name in cloth.items():
        print(name) 
        # ['yellow_hat', 'green_turban']
        # ['blue_sunglasses']
        
        answer *= (len(name)+1)
        
    return answer - 1 

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes)) # 5