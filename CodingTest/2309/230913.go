package main

import (
	"fmt"
)

func solution(cards1 []int, cards2 []int, goal []int) string {
	cards1Idx := 0
	cards2Idx := 0

	for _, i := range goal {
		if cards1Idx < len(cards1) && i == cards1[cards1Idx] {
			cards1Idx++
		} else if cards2Idx < len(cards2) && i == cards2[cards2Idx] {
			cards2Idx++
		} else {
			return "No"
		}
	}

	return "Yes"
}

func main() {
	cards1 := []int{1, 2, 3}
	cards2 := []int{4, 5, 6}
	goal := []int{1, 2, 3, 4, 5, 6}

	result := solution(cards1, cards2, goal)
	fmt.Println(result) // 출력 결과: Yes
}
