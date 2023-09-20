'''
    프로그래머스 : 가장 큰 수 찾기
    https://school.programmers.co.kr/tryouts/85908/challenges
'''

def solution(array):
    answer = [max(array), array.index(max(array))]
        
    return answer

array = [1, 8, 3]
print(solution(array))
# [8, 1]

'''
Golang

package main

import (
	"fmt"
)

func solution(array []int) []int {
  max_num := array[0]
  max_idx := 0

  for idx, num := range array {
    if num > max_num {
      max_num = num
      max_idx = idx
    }
  }

  answer := []int {max_num, max_idx}
  
  return answer
}

func main() {
	array := []int{1, 8, 3}
  result := solution(array)
  fmt.Println(result)
}

'''