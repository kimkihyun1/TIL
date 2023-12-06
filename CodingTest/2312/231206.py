'''
    프로그래머스 : 외계어 사전
    https://school.programmers.co.kr/tryouts/85920/challenges?language=python3
'''

def solution(spell, dic):
    for word in dic:
        if not set(spell) - set(word):
            return 1
    return 2

spell = ["p", "o", "s"]
dic = ["sod", "eocd", "qixm", "adio", "soo"]
print(solution(spell, dic))

'''
Golang

package main

import (
    "fmt"
)

func solution(spell []string, dic []string) int {
  for _, word := range dic {
    if len(word) >= len(spell) {
      find := true
      for _, s := range spell {
        if !contain(word, s) {
          find = false
          break
        }
      }
      if find {
        return 1
      }
    }
  }
  return 2
}

func contain(word string, s string) bool {
  for _, c := range word {
    if string(c) == s {
      return true
    }
  }
  return false
}

func main() {
  spell := []string{"p", "o", "s"}
  dic := []string{"sod", "eocd", "qixm", "adio", "soo"}
  result := solution(spell, dic)
  fmt.Println(result) // 2
}
'''