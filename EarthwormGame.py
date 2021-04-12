import sys

n = (int)(input()) # 정사각형 크기
k = (int)(input()) # 사과의 개수
turnNumber = (int)(input()) # turn 방향전환 횟수

global earthworm    # 지렁이 머리부터 꼬리까지 판에 위치하는 index를 리스트에 저장
earthworm = [[1, 1]]

global earthwormSize    # 지렁이의 크기
earthwormSize = 1

global direction    # 지렁이가 향하는 방향
direction = "R"

global arr      # 판을 위한 2차원 배열
arr = [[0] * (n+2) for i in range(n+2)]     # (n+2) x (n+2) 크기의 2차원 배열 생성


gameTurn = 0    # 지렁이 게임의 현재 turn 수

turnT = []      # 입력받은 지렁이의 방향 전환 정보 중 몇 turn에 방향 전환이 되는지 저장할 리스트
turnD = []      # 입력받은 지렁이의 방향 전환 정보 중 바꿀 방향을 저장할 리스트

def move():     # 지렁이 이동 함수
    global earthworm
    global earthwormSize
    global direction

    newX = earthworm[0][0]  # 지렁이 머리의 x좌표
    newY = earthworm[0][1]  # 지렁의 머리의 y좌표

    if direction == "U":    # 방향이 U 일 경우
        newX = earthworm[0][0] - 1  # 지렁이의 머리가 이동할 자리를 x좌표에서 1 빼서 저장한다
    elif direction == "D":  # 방향이 D 일 경우
        newX = earthworm[0][0] + 1  # 지렁이의 머리가 이동할 자리를 x좌표에서 1 더하고 저장한다.
    elif direction == "L":  # 방향이 L 일 경우
        newY = earthworm[0][1] - 1  # 지렁이의 머리가 이동할 자리를 y좌표에서 1 빼서 저장한다.
    elif direction == "R":  # 방향이 R 일 경우
        newY = earthworm[0][1] + 1  # 지렁이의 머리가 이동할 자리를 y좌표에서 1 더하고 저장한다.

    if arr[newX][newY] == 1:    # 지렁이의 머리가 이동할 위치에 먹이가 있을 경우
        feed(newX,newY)     # 해당하는 위치로 머리가 생성
    elif arr[newX][newY] == -1:     # 지렁이의 머리가 이동할 위치가 판에서 벗어난 경우
        return -10                  # -10 반환
    elif arr[newX][newY] == 2:      # 지렁이의 머리가 이동할 위치에 지렁이 자신의 몸이 있을 경우
       return -10                   # -10 반환
    else:                   # 지렁이의 머리가 이동할 위치에 먹이도 없고, 자신의 몸도 없는 경우
        feed(newX,newY)     # 해당하는 위치로 머리가 생성
        delete()            # 지렁이의 꼬리 부분 삭제

def feed(x,y):      # 해당하는 좌표로 지렁이의 머리를 생성하는 함수
    global earthwormSize
    earthwormSize += 1  # 지렁이의 크기 +1

    earthworm.insert(0, [x,y])  # 지렁이의 머리에 해당하는 새로운 좌표를 지렁이 리스트의 맨 앞에 삽입
    arr[x][y] = 2   # 지렁이의 머리가 새로 생성된 부분 판에서 2로 설정

def delete():   # 지렁이의 꼬리를 삭제하는 함수
    temp = earthworm.pop()      # 지렁이 리스트에서 꼬리 좌표 pop()
    oldX = temp[0]
    oldY = temp[1]
    arr[oldX][oldY] = 0     # 판에서 지렁이의 꼬리가 있던 좌표의 값을 0으로 설정

def changedirection(newDirection):
    global direction

    if newDirection == "L":
        if direction == "U":
            direction = "L"
        elif direction == "D":
            direction = "R"
        elif direction == "L":
            direction = "D"
        elif direction == "R":
            direction = "U"

    elif newDirection == "R":
        if direction == "U":
            direction = "R"
        elif direction == "D":
            direction = "L"
        elif direction == "L":
            direction = "U"
        elif direction == "R":
            direction = "D"

for i in range(k):  # 2차원 배열에 먹이 있는 곳을 1로 표시
    appleX, appleY = map(int,sys.stdin.readline().rstrip().split(" "))
    arr[appleX][appleY] = 1

for i in range(n+2):    # 판 밖은 -1로 초기화
    for j in range(n+2):
        if i == 0 or j == 0 or i == (n+1) or j == (n+1):
           arr[i][j] = -1

for i in range(turnNumber):     # 방향 전환 입력
    T, D = sys.stdin.readline().rstrip().split(" ")
    T = (int)(T)
    turnT.append(T)
    turnD.append(D)

while True:
    value = move()

    gameTurn += 1

    if value == -10:    # 머리의가 판 밖으로 나가거나 자신의 몸에 부딪혔을 경우 게임 끝
        break

    for i in range(turnNumber):
        if gameTurn == turnT[i]:
            changedirection(turnD[i])

print(gameTurn)


'''
5
5
2
4 2
4 3
4 4
4 5
2 5
4 R
5 R
'''

'''
5
5
5
4 2
4 3
4 4
2 5
4 5
1 R
4 L
7 L
8 L
9 L
'''