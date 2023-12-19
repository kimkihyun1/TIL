'''
    프로그래머스 : 신고 결과 받기
    https://school.programmers.co.kr/tryouts/85925/challenges?language=python3
'''

from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    
    report = list(set(report)) # 중복 제거
    user_id = defaultdict(set) # 신고한 id
    count = defaultdict(int) # 신고 횟수
    
    for user in report:
        i, j = user.split() # i : 신고한 유저, j : 신고당한 유저
        user_id[i].add(j) # 신고한 id 추가
        count[j] += 1 # 신고당한 id 횟수 증가
        
    for id_ in id_list:
        cnt = 0
        for u in user_id[id_]:
            if count[u] >= k:  # k번 이상 신고당하면 메일 횟수 증가
                cnt += 1   
        answer.append(cnt)
    
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k)) # [2,1,1,0]

'''
Golang

package main

import (
    "fmt"
    "strings"
)

// 중복 제거 함수
func removeDuplicate(report []string) []string {
    set := make(map[string]struct{})
    var result []string

    for _, user := range report {
        set[user] = struct{}{}
    }

    for s := range set {
        result = append(result, s)
    }

    return result
}

func solution(id_list []string, report []string, k int) []int {
    answer := make([]int, len(id_list))
    report = removeDuplicate(report)
    user_id := make(map[string]map[string]struct{})
    count := make(map[string]int)

    for _, users := range report {
        user := strings.Split(users, " ")
        i, j := user[0], user[1]
        if _, ok := user_id[i]; !ok {
            user_id[i] = make(map[string]struct{})
        }
        user_id[i][j] = struct{}{}
        count[j] += 1
    }

    for idx, id := range id_list {
        cnt := 0
        for i := range user_id[id] {
            if count[i] >= k {
                cnt += 1
            }
        }
        answer[idx] = cnt
    }
    
    return answer
}

func main() {
    id_list := []string{"muzi", "frodo", "apeach", "neo"}
    report := []string{"muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"}
    k := 2
    result := solution(id_list, report, k)
    fmt.Println(result) // [2 1 1 0]
}
'''