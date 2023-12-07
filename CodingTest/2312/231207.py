'''
    프로그래머스 : 중복된 문자 제거
    https://school.programmers.co.kr/tryouts/85921/challenges?language=python3
'''

def solution(my_string):
    answer = ''.join(dict.fromkeys(my_string))
    return answer

my_string = "people"
print(solution(my_string)) # "peol"

'''
Golang

package main

import (
    "fmt"
)

func solution(my_string string) string {
  seen := make(map[rune]struct{})
  var result string

  for _, char := range my_string {
    if _, ok := seen[char]; !ok {
      result += string(char)
      seen[char] = struct{}{}
    }
  }
  
  return result
}

func main() {
  myString := "people"
  result := solution(myString)
  fmt.Println(result) // "peol"
}
'''