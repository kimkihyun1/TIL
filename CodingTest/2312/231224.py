'''
    프로그래머스 : 올바른 괄호
    https://school.programmers.co.kr/tryouts/85929/challenges?language=python3
'''

def solution(s):
    answer = []
    
    for i in s:
        if i == '(':
            answer.append(i)
        else:
            if answer == []:
                return False
            else:
                answer.pop()
    
    return answer == []

s = "(())()"
print(solution(s)) # True

'''
Golang

package main

import (
    "fmt"
)

func solution(s string) bool {
    var answer []rune

    for _, i := range s {
        if i == '(' {
            answer = append(answer, i)
        } else {
            if len(answer) == 0 {
                return false
            } else {
                answer = answer[:len(answer)-1]
            }
        }
    }
    
    return len(answer) == 0
}

func main() {
    s := "(())()"
    result := solution(s)
    fmt.Println(result) // true
}
'''