'''
    프로그래머스 : 완주하지 못한 선수
    https://school.programmers.co.kr/tryouts/85916/challenges?language=python3
'''

def solution(participant, completion):
    hash_dict = {}
    hash_sum = 0
    
    for i in participant:
        hash_dict[hash(i)] = i
        hash_sum += hash(i)
        
    for j in completion:
        hash_sum -= hash(j)
        
    return hash_dict[hash_sum]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))
# leo

'''
Golang

package main

import (
	"fmt"
	"hash/fnv"
)

func solution(participant []string, completion []string) string {
  hash_dict := make(map[uint32]string)
  hash_sum := uint32(0)

  for _, p := range participant {
    h := hash(p)
    hash_dict[h] = p
    hash_sum += h
  }

  for _, c := range completion {
    hash_sum -= hash(c)
  }

  return hash_dict[hash_sum]
}

func hash(s string) uint32 {
  h := fnv.New32a()
  h.Write([]byte(s))
  return h.Sum32()
}


func main() {
	participant := []string{"leo", "kiki", "eden"}
  completion := []string{"eden", "kiki"}
  result := solution(participant, completion)
  fmt.Println(result)
}

'''