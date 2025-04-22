# 전역으로 카운팅을 위한 변수 하나 선언
# 각 요소들을 하나씩 +와 - 연산을 하도록 재귀로 호출
# 마지막 단계에서 최종 합산이 타겟넘버와 일치하는 경우 전역 변수 카운트
count_total = 0 # 전역
def solution(numbers, target):
    answer = 0
    global count_total
    
    get_target(numbers[1:], numbers[0], target)
    get_target(numbers[1:], -numbers[0], target)
    
    answer = count_total
    return answer

def get_target(li, cur_sum, target):
    global count_total
    if len(li) == 1: # 마지막 숫자
        temp1 = cur_sum + li[0]
        temp2 = cur_sum - li[0]
        if temp1 == target:
            count_total += 1
        elif temp2 == target:
            count_total += 1
        return
    
    get_target(li[1:], cur_sum + li[0], target)
    get_target(li[1:], cur_sum - li[0], target)

    return 