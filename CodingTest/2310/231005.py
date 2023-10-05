'''
    프로그래머스 : 전화번호 목록
    https://school.programmers.co.kr/tryouts/85917/challenges?language=python3
'''

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
                return False
    
    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))
# False

'''
Golang

package main

import (
    "fmt"
  "sort"
)

func solution(phone_book []string) bool {
  answer := true
  sort.Strings(phone_book)

  for i := 0; i < len(phone_book)-1; i++ {
    if len(phone_book[i]) < len(phone_book[i+1]) && phone_book[i+1][:len(phone_book[i])] == phone_book[i] {
      return false
    }
  }
  return answer
}

func main() {
  phone_book := []string{"119", "97674223", "1195524421"}
  result := solution(phone_book)
  fmt.Println(result)
}

'''