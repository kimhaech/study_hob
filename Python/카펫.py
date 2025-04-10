# brown + yellow의 합산이 곧 전체 크기 -> 이들을 만들 수 있는 조합(약수)구하기
# 가로 >= 세로
# 구해진 조합에서 가로-2 * 세로-2 의 값이 곧 yellow 수
def solution(brown, yellow):
    answer = []
    sum_val = brown + yellow
    temp_list = get_div_list(sum_val)
    
    answer = check_func(temp_list, yellow)
    
    return answer

# 약수 조합 구하는 함수
def get_div_list(value):
    result = []
    i = 2
    while i*i <= value:
        if value % i == 0: # 약수의 경우
            result.append([value//i, i])
        i+=1
        
    return result

# 최종 검사 함수
def check_func(li, yellow):
    check_list = []
    for item in li:
        w = item[0] # 가로
        h = item[1] # 세로
        if (w-2) * (h-2) == yellow:
            check_list = [w, h]
    return check_list