'''
    프로그래머스 : 숫자 문자열과 영단어
    https://school.programmers.co.kr/tryouts/85915/challenges?language=python3
'''

def solution(s):
    num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for idx, n in enumerate(num):
        s = s.replace(n, str(idx))
    
    return int(s)

s = "one4seveneight"
print(solution(s))
# 1478

'''
Golang

package main

import (
	"fmt"
	"strconv"
	"strings"
)

func solution(s string) int {
  num := []string{"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
  for idx, n := range num {
    s = strings.ReplaceAll(s, n, strconv.Itoa(idx))
  }

  result, err := strconv.Atoi(s)
  if err != nil {
    return 0
  }
  
  return result
}

func main() {
	s := "one4seveneight"
  result := solution(s)
  fmt.Println(result)
}

'''