# 효율성 실패 case
# 통으로 길이만큼 비교
def solution(phone_book):
    answer = True
    phone_book.sort(key = lambda x:len(x))
    
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            len_cur = len(phone_book[i])
            temp_val = phone_book[j]
            if phone_book[i] == temp_val[:len_cur]:
                return False
    
    return answer

# 일반 정렬
# 더 짧은 길이의 번호를 기준으로 앞 혹은 뒤의 값만 비교 -> 정렬을 해 놓은 순간 바로 앞 혹은 뒤의 값에서 결과가 나오지 않으면 다른 값은 비교 할 필요가 없음
def solution(phone_book):
    answer = True
    
    phone_book.sort()
    for i in range(len(phone_book)-1):
        len_a = len(phone_book[i])
        len_b = len(phone_book[i+1])
        longer = len_a if len_a < len_b else len_b
        if phone_book[i][:longer] == phone_book[i+1][:longer]:
            return False
        
    return answer