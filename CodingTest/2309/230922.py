'''
    프로그래머스 : 모의고사
    https://school.programmers.co.kr/tryouts/85909/challenges?language=python3
'''

def solution(answers):
    answer = [0, 0, 0]
    std1 = [1, 2, 3, 4, 5]
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = []
    
    for idx, ans in enumerate(answers):
        if ans == std1[idx % len(std1)]:
            answer[0] += 1
        if ans == std2[idx % len(std2)]:
            answer[1] += 1
        if ans == std3[idx % len(std3)]:
            answer[2] += 1
    
    for idx, ans in enumerate(answer):
        if ans == max(answer):
            result.append(idx+1)
    
    return result

answers = [1,3,2,4,2]
print(solution(answers))
# [1, 2, 3]

'''
Golang

package main

import (
	"fmt"
)

func solution(answers []int) []int {
  answer := [3]int{0, 0, 0}
  std1 := []int{1, 2, 3, 4, 5}
  std2 := []int{2, 1, 2, 3, 2, 4, 2, 5}
  std3 := []int{3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
  result := []int{}

  for idx, ans := range answers {
    if ans == std1[idx % len(std1)] {
      answer[0]++
    }
    if ans == std2[idx % len(std2)] {
      answer[1]++
    }
    if ans == std3[idx % len(std3)] {
      answer[2]++
    }
  }

  max_result := max(answer)
  for idx, ans := range answer {
    if ans == max_result {
      result = append(result, idx+1)
    }
  }

  return result
}

func max(answer [3]int) int {
  max_result := answer[0]
  for _, result := range answer {
    if result > max_result {
      max_result = result
    }
  }

  return max_result
}

func main() {
	answers := []int{1, 3, 2, 4, 2}
  result := solution(answers)
  fmt.Println(result)
}

'''