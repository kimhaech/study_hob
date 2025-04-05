# 소수인지 검사하는 함수 필요
# 1. 문자열 값 -> list
# 2. 앞에 0이 붙는 경우 처리 -> 정수형 변환
# 3. 중복제거 - set 변환
# 순열을 만든다 -> 1. itertools의 permutaions 사용 / 2. 자체적으로 만들기
def solution(numbers):
    answer = 0
    numbers = list(numbers) # 문자열 -> 리스트로 만들기
    result_list = []
    
    for i in range(len(numbers)):
        temp = make_permutation(numbers, i+1) # 리스트에서 n개의 값으로 만든 순열
        result_list.append(temp)
    
    f_list = []
    for j in range(len(result_list)):
        result_list[j] = list(map(int, result_list[j]))
        for k in result_list[j]:
            f_list.append(k)
    f_list = list(set(f_list))
    for val in f_list:
        if isPrime(val):
            answer += 1

    return answer

# 순열 만들기 - return list
def make_permutation(arr, pick_count):
    temp_list = []
    if pick_count == 1: # 1개를 뽑는 경우
        return arr
        #return list(map(change_list_val,arr))
    else: # 2개 이상의 값을 뽑는다
        for i in range(len(arr)):
            new_list = arr[:i] + arr[i+1:] # arr[i]를 제외한 리스트
            temp = make_permutation(new_list, pick_count-1) # 선택하는 갯수 - 1개 선택하도록
            for j in range(len(temp)):
                temp_list.append(arr[i] + temp[j])
    return temp_list

# 소수 확인 함수
def isPrime(number): # 소수 판별 함수
    if number == 0 or number == 1:
        return False
    i = 2
    while i*i <= number:
        if number % i == 0:
            return False
        i += 1
        
    return True
# def isPrime(number):
#     if number == 0 or number == 1:
#         return False
#     half_num = number//2 + 1

#     for i in range(2, half_num):
#         if number % i == 0: # 약수 인 경우 (나머지가 0)
#             return False
#     return True
# 소수 판별함수에서 i*i <= number 로 검사하는 이유
# number를 만드는 조합을 보면 항상 두 값 중에 하나는 작거나, 둘 다 같은 경우가 있는데, 이 경우에서 해당 수의 제곱값의 이하이다.
# ex) 36 => 2x18, 3x12, 4x9, 6x6
# ex) 48 => 2x24, 3x16, 4x12, 6x8

from itertools import permutations

def solution(numbers):
    answer = 0
    numbers = list(numbers) # 문자열 -> 리스트로 만들기
    result_list = []
    for i in range(len(numbers)):
        temp_list = list(permutations(numbers,i+1))
        temp_list = list(map(int,list(map(make_string,temp_list))))
        result_list.extend(temp_list)

    result_list = set(result_list)
    for val in result_list:
        if isPrime(val):
            answer += 1
            
    return answer

# 문자열 변환
def make_string(val):
    return ''.join(val)
    
# 소수 확인 함수
def isPrime(number): # 소수 판별 함수
    if number == 0 or number == 1:
        return False
    i = 2
    while i*i <= number:
        if number % i == 0:
            return False
        i += 1
        
    return True