'''
    프로그래머스 : 행렬의 덧셈
    https://school.programmers.co.kr/tryouts/85910/challenges?language=python3
'''

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arr = []
        for j in range(len(arr1[0])):
            arr.append(arr1[i][j] + arr2[i][j])
        answer.append(arr)
    return answer

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]	
print(solution(arr1, arr2))
# [[4,6],[7,9]]