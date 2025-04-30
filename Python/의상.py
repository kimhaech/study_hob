# 각 부위별 입는 옷의 조합의 총 수
# 부위별로는 1개 까지만 입을 수 있음
# 모든 조합은 달라야한다
# 결국 한 부위당 선택지는 -> 각 하나씩 입기 + 안입음
# 그렇다면 조합을 만들 때 부위의 옷 개수 +1 을 두고 전체 곱셈을 진행
# 그리고 겹치는 1개를 뺀다 -> 아무것도 안입는 경우 하나
def solution(clothes):
    answer = 0
    categ = {}
    
    for v in clothes:
        if v[1] in categ:
            categ[v[1]] += 1
        else:
            categ[v[1]] = 1
    
    temp = 1
    for key, val in categ.items():
        temp *= (val+1)
        
    answer = temp-1
    
    return answer