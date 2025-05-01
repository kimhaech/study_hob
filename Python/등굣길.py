# 배열을 하나씩 돌면서 해당 좌표값에 올 수 있는 경우의 수를 더해준다.
# 위, 왼쪽 방향에서 올 수 있는 가능성이 있음
# 계속 값에 mod로 나머지 연산 -> 값이 너무 크면 효율성이 떨어질 수 있음
# 계속 mod로 나누면 결과가 같은게 맞나? - 아래는 항상 성립한다.
# (a + b) % m = ((a % m) + (b % m)) % m
# (a * b) % m = ((a % m) * (b % m)) % m 

def solution(m, n, puddles):
    answer = 0
    route = [[0 for _ in range(m)] for _ in range(n)] # 경로 맵 
    mod = 1000000007
    
    for pud in puddles: # 웅덩이 표시
        route[pud[1]-1][pud[0]-1] = -1
    
    route[0][0] = 1 # 시작점
    
    for i in range(n): # 행의 수
        for j in range(m): # 열의 수
            if i == 0 and j == 0: # 시작점인 경우
                continue
            elif route[i][j] == -1: # 웅덩인 경우
                continue
            if i != 0 and route[i-1][j] != -1: # 위에서 내려옴, 웅덩이 아님
                route[i][j] += route[i-1][j] % mod
            if j != 0 and route[i][j-1] != -1: # 왼쪽에서 옴, 웅덩이 아님
                route[i][j] += route[i][j-1] % mod
                
    answer = route[n-1][m-1] % mod
    
    return answer

    