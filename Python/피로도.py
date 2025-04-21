# permutations 사용 - 순열
# 중복 x, 순서 o
# 모든 경우의 수를 만들고, 해당 경우의 수를 따라서 탐색하도록 한 뒤 최대값을 가져온다.
from itertools import permutations 

def solution(k, dungeons):
    answer = -1
    temp = []
    for i in range(len(dungeons)):
        temp.append(i)
    temp_per = list(permutations(temp, len(temp)))
    
    for li in temp_per:
        t_ans = find_route(li, dungeons, k)
        if answer < t_ans:
            answer = t_ans
    return answer

def find_route(li, dungeons, k):
    count = 0
    temp_p = k
    for i in li:
        dun = dungeons[i]
        if temp_p >= dun[0]: # 잔여 피로도가 필요 필요도 이상
            temp_p -= dun[1]
            count += 1
        else:
            return count
    return count
        