# 중복 순열을 통해서 찾기
# 모음 list갯수 만큼 순차적으로 중복될 수 있게 모든 단어 조합을 만든다.
# 해당 리스트의 정렬 후 주어진 단어의 index를 찾아서 +1 하면 n번째인지 확인 가능
from itertools import product

def solution(word):
    answer = 0
    word_list = ['A','E','I','O','U']
    temp = []
    for i in range(1,6):    
        temp.extend(list(product(word_list, repeat=i)))
    
    temp_word = [''.join(w) for w in temp]
    temp_word.sort()
    answer = temp_word.index(word) + 1
    return answer