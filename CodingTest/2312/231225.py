'''
    프로그래머스 : 배열 회전시키기
    https://school.programmers.co.kr/tryouts/85930/challenges?language=python3
'''

def solution(numbers, direction):
    answer = []
    if direction == "right":
        answer = [numbers[-1]] + numbers[:len(numbers)-1]
    else:
        answer = numbers[1:] + [numbers[0]]
        
    return answer

numbers = [1, 2, 3]
direction = "right"
print(solution(numbers, direction)) # [3, 1, 2]

'''
Golang

package main

import (
    "fmt"
)

func solution(numbers []int, direction string) []int {
    var answer []int

    if direction == "right" {
        answer = append([]int{numbers[len(numbers)-1]}, numbers[:len(numbers)-1]...)
    } else {
        answer = append(numbers[1:], numbers[0])
    }

    return answer
}

func main() {
    numbers := []int{1, 2, 3}
    direction := "right"
    result := solution(numbers, direction)
    fmt.Println(result) // [3 1 2]

}
'''