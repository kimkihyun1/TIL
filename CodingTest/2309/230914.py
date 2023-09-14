'''
    프로그래머스 :  로또의 최고 순위와 최저 순위
    https://school.programmers.co.kr/tryouts/85904/challenges?language=python3
'''

def solution(lottos, win_nums):
    answer = []
    count = 0
    if sum(lottos) == 0:
        return [1, 6]
    for i in lottos:
        if i in win_nums:
            count += 1
    zero_num = lottos.count(0)
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    answer = [rank[count+zero_num], rank[count]]
    
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))
# [3, 5]

'''
Golang

package main

import "fmt"

func solution(lottos []int, winNums []int) []int {
    answer := make([]int, 2)
    count := 0

    // 모든 로또 번호가 0이면 [1, 6]을 반환
    if sum(lottos) == 0 {
        return []int{1, 6}
    }

    for _, num := range lottos {
        if contains(winNums, num) {
            count++
        }
    }

    zeroCount := countZero(lottos)
    rank := map[int]int{6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    answer[0] = rank[count+zeroCount]
    answer[1] = rank[count]

    return answer
}

func sum(nums []int) int {
    total := 0
    for _, num := range nums {
        total += num
    }
    return total
}

func contains(arr []int, target int) bool {
    for _, num := range arr {
        if num == target {
            return true
        }
    }
    return false
}

func countZero(nums []int) int {
    count := 0
    for _, num := range nums {
        if num == 0 {
            count++
        }
    }
    return count
}

func main() {
    lottos := []int{44, 1, 0, 0, 31, 25}
    winNums := []int{31, 10, 45, 1, 6, 19}
    result := solution(lottos, winNums)
    fmt.Println(result) // 출력 결과: [3 5]
}

'''