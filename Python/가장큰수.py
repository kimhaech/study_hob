# x*3 ? -> 비교대상 x를 3자리까지 같은 수로 비교하도록 한 것
# '3', '30', '34' -> '333', '303030', '343434'
# 문제에서 최대가 1000이기에 3자리까지 비교할 수 있게(1000은 4자리인데? -> 4자리는 1000뿐이고 100까지만 비교해도 문제 없기떄문)
def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key = lambda x:x*3)
    
    answer = ''.join(numbers)
    if answer[0] == '0': 
        return '0'
    else:
        return answer


# 다른버전 -> import를 해야한다는 문제
# 기존 아이디어였음 -> 앞과 뒤의 문자를 더해서 비교했을 때 큰 수를 앞으로, 작은 수를 뒤로 보내는 방식
from functools import cmp_to_key

def custom_compare(x, y):
    if x + y > y + x:
        return -1  # x가 앞에 와야 함
    elif x + y < y + x:
        return 1   # y가 앞에 와야 함
    else:
        return 0   # 동일하면 순서 유지

def solution(numbers):
    # 숫자를 문자열로 변환
    numbers = list(map(str, numbers))

    # 비교 함수 기반 정렬 (내림차순)
    numbers.sort(key=cmp_to_key(custom_compare))

    # 결과 문자열로 변환 후 반환
    answer = ''.join(numbers)
    
    # "000..."과 같은 경우 "0"으로 변환
    return "0" if answer[0] == "0" else answer