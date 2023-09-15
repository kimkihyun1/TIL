'''
    프로그래머스 : 잘라서 배열로 저장하기
    https://school.programmers.co.kr/tryouts/85905/challenges?language=python3
'''

def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i+n])
    return answer

my_str = "abc1Addfggg4556b"
n = 6
print(solution(my_str, n))
# ["abc1Ad", "dfggg4", "556b"]

'''
Golang

package main

import (
	"fmt"
)

func solution(my_str string, n int) []string {
  var answer []string
  for i := 0; i < len(my_str); i += n {
    end := i + n
    if end > len(my_str) {
      end = len(my_str)
    }
    answer = append(answer, my_str[i:end])
  }
  
  return answer
}

func main() {
	my_str := "abc1Addfggg4556b"
  n := 6
  result := solution(my_str, n)
  fmt.Println(result)
}

'''