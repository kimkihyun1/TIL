'''
    프로그래머스 : 같은 숫자는 싫어
    https://school.programmers.co.kr/tryouts/85927/challenges?language=python3
'''

def solution(arr):
    answer = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
        
    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr)) # [1,3,0,1]

'''
Golang

package main

import (
    "fmt"
)

func solution(arr []int) []int {
    var answer []int
    if len(arr) > 0 {
        answer = append(answer, arr[0])
    }

    for i := 1; i < len(arr); i++ {
        if arr[i] != arr[i-1] {
            answer = append(answer, arr[i])
        }
    }
    
    return answer
} 

func main() {
    arr := []int{1, 1, 3, 3, 0, 1, 1}
    result := solution(arr)
    fmt.Println(result) // [1 3 0 1]
}
'''