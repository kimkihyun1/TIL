'''
    프로그래머스 : 베스트 앨범
    https://school.programmers.co.kr/tryouts/85919/challenges
'''

def solution(genres, plays):
    answer = []
    dic1 = {}
    dic2 = {}
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic1:
            dic1[genre] = [(idx, play)]
        else:
            dic1[genre].append((idx, play))
        if genre not in dic2:
            dic2[genre] = play
        else:
            dic2[genre] += play
            
    for (k, v) in sorted(dic2.items(), key=lambda x: x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)
        
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))
# [4, 1, 3, 0]

'''
Golang

package main

import (
    "fmt"
    "sort"
)

func solution(genres []string, plays []int) []int {
    var answer []int
    dic1 := make(map[string][]struct{ idx, play int })
    dic2 := make(map[string]int)

    for idx, genre := range genres {
        play := plays[idx]
        dic1[genre] = append(dic1[genre], struct{ idx, play int }{idx, play})
        dic2[genre] += play
    }

    sortedGenres := make([]string, 0, len(dic2))
    for k := range dic2 {
        sortedGenres = append(sortedGenres, k)
    }
    sort.Slice(sortedGenres, func(i, j int) bool {
        return dic2[sortedGenres[i]] > dic2[sortedGenres[j]]
    })

    for _, k := range sortedGenres {
        sort.Slice(dic1[k], func(i, j int) bool {
            return dic1[k][i].play > dic1[k][j].play
        })

        count := 0
        for _, p := range dic1[k] {
            if count >= 2 {
                break
            }
            answer = append(answer, p.idx)
            count++
        }
    }

    return answer
}

func main() {
    genres := []string{"classic", "pop", "classic", "classic", "pop"}
    plays := []int{500, 600, 150, 800, 2500}
    result := solution(genres, plays)
    fmt.Println(result) // 출력 결과: [4 1 3 0]
}

'''