'''
    프로그래머스 : 바탕화면 정리
    https://school.programmers.co.kr/tryouts/85911/challenges?language=python3
'''

def solution(wallpaper):
    x = []
    y = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                x.append(i)
                y.append(j)
    
    answer = [min(x), min(y), max(x)+1, max(y)+1]
    
    return answer

wallpaper = [".#...", "..#..", "...#."]
print(solution(wallpaper))
# [0, 1, 3, 4]

'''
Golang

package main

import (
	"fmt"
)

func solution(wallpaper []string) []int {
  var x []int
  var y []int

  for i := 0; i < len(wallpaper); i++ {
    for j := 0; j < len(wallpaper[i]); j++ {
      if wallpaper[i][j] == '#' {
        x = append(x, i)
        y = append(y, j)
      }
    }
  }

  minX, maxX := min_max(x) 
  minY, maxY := min_max(y)
  answer := []int{minX, minY, maxX + 1, maxY + 1}
  
  return answer
}

func min_max(arr []int) (int, int) {
  if len(arr) == 0 {
    return 0, 0
  }
  minVal := arr[0]
  maxVal := arr[0]

  for _, ans := range arr {
    if ans < minVal {
      minVal = ans
    }
    if ans > maxVal {
      maxVal = ans
    }
  }

  return minVal, maxVal
}

func main() {
  wallpaper := []string{".#...", "..#..", "...#."}
  result := solution(wallpaper)
  fmt.Println(result)
}

'''