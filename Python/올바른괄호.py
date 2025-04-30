# 스택에 괄호를 순서대로 하나씩 push
# 다음 괄호를 넣기 전 짝이 맞는 경우 pop 하기
# 마지막 반복까지 끝낸 후 스택에 남은 괄호가 있으면 false
# 추가로 맨앞 혹은 마지막의 값이 맞지 않는 경우는 미리 차단
def solution(s):
    answer = True
    check_stack = []
    if s[0] == ')' or s[-1] == '(':
        return False
    
    for c in s:
        if len(check_stack) > 0:
            if c == ')' and check_stack[-1] == '(': # 마지막이 여는 괄호
                check_stack.pop()
            else:
                check_stack.append(c)
        else:
            check_stack.append(c)
    
    if len(check_stack) > 0:
        return False
    return True