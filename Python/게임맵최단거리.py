from collections import deque

# bfs 알고리즘 사용
# 방문 예정 좌표를 큐로 관리 -> 큐에서 하나씩 빼면서 다음 방문을 할 위치의 베이스로 지정
# 방문처리를 하는 리스트에 이전 방문 좌표의 카운트에 +1을 해주는 방식으로 횟수 관리
def solution(maps):
    answer = 0
    qu = deque() # 방문 예정 좌표를 저장할 큐
    len_w = len(maps[0]) # 열의 수
    len_h = len(maps) # 행의 수
    visit_list = [[0 for _ in range(len_w)] for _ in range(len_h)] # 방문 기록
    mov_list = [[0,1], [0,-1], [1,0], [-1,0]] # 이동 범위
    
    qu.append([0,0])
    visit_list[0][0] = 1
    
    while qu:
        c_x, c_y = qu.popleft() # 현재 x,y 좌표(이전 반복에서 방문 예정인 좌표인 것)
        for mv in mov_list: # 각 범위별로 방문하기
            n_x = c_x + mv[0]
            n_y = c_y + mv[1]
            if 0<=n_x<len_h and 0<=n_y<len_w and visit_list[n_x][n_y] == 0 and maps[n_x][n_y] == 1: # 범위 초과 x, 방문 이력 x, 막혀있지 x
                qu.append([n_x, n_y]) # 방문 예정(탐색) 큐에 추가
                visit_list[n_x][n_y] = visit_list[c_x][c_y] + 1 # 방문 체크
                
    if visit_list[len_h - 1][len_w - 1] == 0: # 방문 x
        return -1
    else:
        return visit_list[len_h - 1][len_w - 1]