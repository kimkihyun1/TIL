'''
    프로그래머스 : 7의 개수
    https://school.programmers.co.kr/tryouts/85907/challenges?language=python3
'''

def solution(array):
    answer = 0
    for i in array:
        answer += str(i).count('7')
    return answer

array = [7, 77, 17]
print(solution(array))
# 4

'''
Golang

package main

import (
	"fmt"
	"strconv"
	"strings"
)


func solution(array []int) int {
  answer := 0
  for _, num := range array {
    answer += strings.Count(strconv.Itoa(num), "7")
  }
  
  return answer
}

func main() {
	array := []int{7, 77, 17}
  result := solution(array)
  fmt.Println(result)
}

'''