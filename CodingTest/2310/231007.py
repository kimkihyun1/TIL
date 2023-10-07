'''
    프로그래머스 : 의상
    https://school.programmers.co.kr/tryouts/85918/challenges?language=python3
'''

def solution(clothes):
    answer = 1
    hash_clothes = {}
    for _, kind in clothes:
        hash_clothes[kind] = hash_clothes.get(kind, 0) + 1
    
    for kind in hash_clothes:
        answer *= hash_clothes[kind] + 1
    
    return answer - 1 

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
# 5

'''
Golang

package main

import (
	"fmt"
)

func solution(clothes [][]string) int {
  answer := 1
  hash_clothes := make(map[string]int)

  for _, cloth := range clothes {
    kind := cloth[1]
    hash_clothes[kind]++
  }

  for _, cnt := range hash_clothes {
    answer *= cnt + 1
  }

  return answer - 1
}

func main() {
  clothes := [][]string{{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}}
  result := solution(clothes)
  fmt.Println(result)
}

'''
