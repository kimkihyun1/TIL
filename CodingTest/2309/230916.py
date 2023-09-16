'''
    프로그래머스 : 2차원으로 만들기
    https://school.programmers.co.kr/tryouts/85906/challenges?language=python3
'''

def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    return answer

num_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2
print(solution(num_list, n))
# [[1, 2], [3, 4], [5, 6], [7, 8]]

'''
Golang

package main

import (
	"fmt"
)

func solution(num_list []int, n int) [][]int {
  var answer [][]int

  for i := 0; i < len(num_list); i += n {
    end := i + n
    if end > len(num_list) {
      end = len(num_list)
    }
    answer = append(answer, num_list[i:end])
  }
  
  
  return answer
}

func main() {
	num_list := []int{1, 2, 3, 4, 5, 6, 7, 8}
  n := 2
  result := solution(num_list, n)
  fmt.Println(result)
}

'''