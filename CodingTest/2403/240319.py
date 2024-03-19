'''
    프로그래머스 : 최고의 집합
    https://school.programmers.co.kr/tryouts/85963/challenges?language=python3
'''

def solution(n, s):
    # q : 몫, r : 나머지
    q, r = divmod(s, n)
    
    if not q:
        return [-1]
    
    # 곱해서 가장 큰 수가 나올려면 몫과 몫 + 1이 필요하다
    # 나머지가 0일 경우는 몫 2번 필요하다 
    answer = [q for _ in range(n - r)] + [q + 1 for _ in range(r)]
    
    return answer

n = 2
s = 9
print(solution(n, s)) # [4, 5]
