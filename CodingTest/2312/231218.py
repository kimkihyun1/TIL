'''
    프로그래머스 : 둘만의 암호
    https://school.programmers.co.kr/tryouts/85924/challenges?language=python3
'''

def solution(s, skip, index):
    answer = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # 알파벳 제거
    for i in skip:
        if i in alphabet:
            alphabet = alphabet.replace(i, "")
            
    # 알파벳 이동
    for j in s:
        a = alphabet[(alphabet.index(j) + index) % len(alphabet)]
        answer += a
    
    return answer

s = "aukks"
skip = "wbqd"
index = 5
print(solution(s, skip, index)) # happy

'''
Golang

package main

import (
  "fmt"
  "strings"
)

func solution(s string, skip string, index int) string {
  answer := ""
  alphabet := "abcdefghijklmnopqrstuvwxyz"

  // 알파벳 제거
  for _, i := range skip {
    if strings.ContainsRune(alphabet, i) {
      alphabet = strings.Replace(alphabet, string(i), "", -1)
    }
  }

  // 알파벳 이동
  for _, j := range s {
    idx := (strings.Index(alphabet, string(j)) + index) % len(alphabet)
    a := string(alphabet[idx])
    answer += a
  }
  return answer
}

func main() {
  s := "aukks"
  skip := "wbqd"
  index := 5
  result := solution(s, skip, index)
  fmt.Println(result) // happy
}
'''