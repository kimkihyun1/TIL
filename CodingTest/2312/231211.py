'''
    프로그래머스 : 폰켓몬
    https://school.programmers.co.kr/tryouts/85923/challenges?language=python3
'''

def solution(nums):
    if len(nums) / 2 > len(set(nums)):
        return len(set(nums))
    else:
        return len(nums) // 2
    
nums = [3,1,2,3]
print(solution(nums)) # 2

'''
Golang

package main

import (
    "fmt"
)

func solution(nums []int) int {
  set := make(map[int]struct{})

  for _, num := range nums {
    set[num] = struct{}{}
  }

  if len(nums) / 2 > len(set) {
    return len(set) 
  } else {
    return len(nums) / 2
  }
}

func main() {
  nums := []int{3, 1, 2, 3}
  result := solution(nums)
  fmt.Println(result) // 2
}
'''