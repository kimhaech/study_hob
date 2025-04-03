# 가로 세로의 큰 값을 1번으로 작은 값은 2번으로
# 1,2번의 최대값을 뽑아서 사용
# 혹은? 변수 두개에 최대값을 만들어서 사용
def solution(sizes):
    answer = 0
    left = []
    right = []
    for size in sizes:
        if size[0] > size[1]:
            left.append(size[0])
            right.append(size[1])
        else:
            left.append(size[1])
            right.append(size[0])
    answer = max(left) * max(right)
    return answer