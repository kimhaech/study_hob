# 스택 사용
# 스택에 값이 있고, 스택의 마지막 값(이전의 주식 가격을 가지는 인덱스) > 현재 값
# 위 경우에는 주가가 떨어진 것으로 본다 -> 스택의 값을 pop하고 현재 값의 인덱스 - 해당 인덱스를 한다.
# 현재 값의 인덱스 - pop 하게 된 인덱스 => 주가가 떨어지지 않은 시간
def solution(prices):
    answer = [0 for _ in range(len(prices))]
    st = []
    
    for i in range(len(prices)):
        # 이전의 주가보다 현재 가격이 떨어진 값인 경우
        while st and prices[st[-1]] > prices[i]: 
            temp_ind = st.pop()
            tm = i - temp_ind
            answer[temp_ind] = tm
        st.append(i)
    
    while st:
        temp_ind = st.pop()
        tm = i - temp_ind
        answer[temp_ind] = tm
    
    return answer