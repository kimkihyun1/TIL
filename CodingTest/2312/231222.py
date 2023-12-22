'''
    프로그래머스 : 햄버거 만들기
    https://school.programmers.co.kr/tryouts/85928/challenges?language=python3
'''

def solution(ingredient):
    answer = 0
    lst = []
    for i in ingredient:
        lst.append(i)
        if lst[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                lst.pop()
    
    return answer

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))

'''
Golang

package main

import (
    "fmt"
)

func solution(ingredient []int) int {
    answer := 0
    var lst []int

    for _, i := range ingredient {
        lst = append(lst, i)
        if len(lst) >= 4 && [4]int{lst[len(lst)-4], lst[len(lst)-3], lst[len(lst)-2], lst[len(lst)-1]} == [4]int{1, 2, 3, 1} {
            answer++
            for j := 0; j < 4; j++ {
                lst = lst[:len(lst)-1]
            }
        }
    }
    
    return answer
}

func main() {
    ingredient := []int{2, 1, 1, 2, 3, 1, 2, 3, 1}
    result := solution(ingredient)
    fmt.Println(result) // 2
}
'''