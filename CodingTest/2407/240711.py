'''
    프로그래머스 : 베스트앨범
    https://school.programmers.co.kr/learn/courses/30/lessons/42579
'''

def solution(genres, plays):
    answer = []
    total_dict = {}
    genre_dict = {}
    
    for i in range(len(genres)):
        total_dict[genres[i]] = total_dict.get(genres[i], 0) + plays[i]
        genre_dict[genres[i]] = genre_dict.get(genres[i], []) + [(plays[i], i)]
        
    print(total_dict) # {'classic': 1450, 'pop': 3100}
    print(genre_dict) # {'classic': [(500, 0), (150, 2), (800, 3)], 'pop': [(600, 1), (2500, 4)]}
    
    genre_sort = sorted(total_dict.items(), key=lambda x: x[1], reverse=True)
    print(genre_sort) # [('pop', 3100), ('classic', 1450)]
    
    for (genre, _) in genre_sort:
        genre_dict[genre] = sorted(genre_dict[genre], key=lambda x: (-x[0], x[1]))
        answer += [num for (_, num) in genre_dict[genre][:2]]
    
    print(genre_dict) # {'classic': [(800, 3), (500, 0), (150, 2)], 'pop': [(2500, 4), (600, 1)]}
    
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays)) # [4, 1, 3, 0]