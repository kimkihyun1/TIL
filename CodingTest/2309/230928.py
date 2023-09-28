'''
    프로그래머스 : 가장 가까운 같은 글자
    https://school.programmers.co.kr/tryouts/85914/challenges?language=python3
'''

def solution(s):
    answer = []
    word_dict = {}
    
    for i in range(len(s)):
        if s[i] not in word_dict:
            answer.append(-1)
        else:
            answer.append(i-word_dict[s[i]])
        word_dict[s[i]] = i # 가까운 것으로 갱신
            
    return answer

s = "banana"
print(solution(s))
# [-1, -1, -1, 2, 2, 2]

'''
Golang

package main

import (
	"fmt"
)

func solution(s string) []int {
  var answer []int
  word_dict := make(map[rune]int)

  for i, word := range s {
    if idx, w := word_dict[word]; !w {
      answer = append(answer, -1)
    } else {
      answer = append(answer, i - idx)
    }
    word_dict[word] = i
  }
  return answer
}

func main() {
	s := "banana"
  result := solution(s)
  fmt.Println(result)
}

'''