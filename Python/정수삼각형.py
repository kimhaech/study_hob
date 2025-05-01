# 삼각형 바닥부터 올라오기
# 가장 아랫줄은 건들지 x
# 아래서 두번째부터 시작 -> 아래의 선택할 수 있는 두 원소 중 큰 값과 더한 값이 현재 값
# 타고 올라가면 결국 꼭대기의 값이 최대값
def solution(triangle):
    answer = 0

    for i in range(len(triangle)-2, -1, -1): # 바닥부터 올라오기
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

    answer = triangle[0][0]
    return answer