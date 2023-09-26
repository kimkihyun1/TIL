'''
    프로그래머스 : 로그인 성공
    https://school.programmers.co.kr/tryouts/85912/challenges?language=python3
'''

def solution(id_pw, db):
    for lst in db:
        if lst[0] == id_pw[0]:
            if lst[1] == id_pw[1]:
                return 'login'
            return 'wrong pw'

    return 'fail'

id_pw = ["meosseugi", "1234"]
db = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]
print(solution(id_pw, db))
# login

'''
Golang

package main

import (
	"fmt"
)

func solution(id_pw []string, db [][]string) string {
    for _, lst := range db {
      if lst[0] == id_pw[0] {
          if lst[1] == id_pw[1] {
              return "login"
          }
          return "wrong pw"
      }
  }
  return "fail"
}

func main() {
	id_pw := []string{"meosseugi", "1234"}
  db := [][]string{{"rardss", "123"}, {"yyoom", "1234"}, {"meosseugi", "1234"}}
  result := solution(id_pw, db)
  fmt.Println(result)
}

'''