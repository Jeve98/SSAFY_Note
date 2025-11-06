import sys
sys.stdin = open('algo/input.txt', 'r')

from collections import deque

# print(ord('*')) # 42
# print(ord('.')) # 46
# print(ord('$')) # 36
# print(ord('A')) # 65
# print(ord('Z')) # 90
# print(ord('a')) # 97


def opening(key):
    if key == '0':
        return
        
    temp = ord(key) - ord('A') - alpha

    for pos in door[temp]:
        board[pos[0]][pos[1]] = '.'

        if pos[0] == 0 or pos[0] == row - 1 or pos[1] == 0 or pos[1] == col - 1:
            entrance.append(pos)

    return


def BFS(pos):
    global count

    queue = deque()
    visited = [[False] * col for _ in range(row)]

    queue.append(pos)
    visited[pos[0]][pos[1]] = True

    find = False
    while queue:
        now = queue.popleft()

        for addI, addJ in zip(di, dj):
            ni = now[0] + addI
            nj = now[1] + addJ

            if 0 <= ni < row and 0 <= nj < col and not visited[ni][nj] and (board[ni][nj] in ['.', '$'] or ord(board[ni][nj]) - ord('a') >= 0):
                queue.append([ni, nj])
                visited[ni][nj] = True

                if ord(board[ni][nj]) - ord('a') >= 0:
                    opening(board[ni][nj])
                    board[ni][nj] = '.'
                    find = True
                elif board[ni][nj] == '$':
                    count += 1
                    board[ni][nj] = '.'
    
    return find


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

tCase = int(input())
for test in range(tCase):
    row, col = map(int, input().split())

    board = [0] * row

    entrance = []
    inventory = []
    door = [[] for _ in range(26)]
    count = 0

    for i in range(row):
        board[i] = list(input())

        for j in range(col):
            if (board[i][j] in ['.', '$'] or ord(board[i][j]) - ord('a') >= 0) and (i == 0 or i == row - 1 or j == 0 or j == col - 1):
                entrance.append([i, j])
                if board[i][j] == '$':
                    count += 1
                    board[i][j] = '.'
                elif ord(board[i][j]) - ord('a') >= 0:
                    inventory.append(board[i][j])
                    board[i][j] = '.'

            temp = ord(board[i][j]) - ord('A')          
            if 25 >= temp >= 0:
                door[temp].append([i, j])
            
    inventory.extend(list(input()))
    alpha = ord('a') - ord('A')
    for key in inventory:
        opening(key)
    
    while True:
        # 입구가 없는 경우
        if not entrance:
            break

        new = False
        for one in entrance:
            # BFS로 매번 확인
            # 새로운 열쇠 획득 시, 문 개방 및 획득 표시
            # 문서 획득 시, count 증가 및 문서 삭제
            find = BFS(one)
            if not new:
                new = find
        
        # 획득 표시가 없는 경우 == 추가적인 변화가 없는 경우, 탐색 종료
        if not new:
            break
    
    print(count)