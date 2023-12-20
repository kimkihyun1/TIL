'''
    프로그래머스 : 컨트롤 제트
    https://school.programmers.co.kr/tryouts/85926/challenges?language=python3
'''

def solution(s):
    answer = 0
    s = s.split()
    
    for i in range(len(s)):
        if s[i] == "Z":
            answer -= int(s[i-1])
        else:
            answer += int(s[i])
    
    return answer

s = "1 2 Z 3"
print(solution(s)) # 4

'''
Golang

package main

import (
    "fmt"
    "strings"
    "strconv"
)

func solution(s string) int {
    answer := 0
    list_s := strings.Fields(s)

    for i := range list_s {
        if list_s[i] == "Z" {
            a, err := strconv.Atoi(list_s[i-1])
            if err == nil {
                answer -= a
            }
        } else {
            b, err := strconv.Atoi(list_s[i])
            if err == nil {
                answer += b
            }
        }
    }
    
    return answer
}

func main() {
    s := "1 2 Z 3"
    result := solution(s)
    fmt.Println(result) // 4
}
'''