C = int(input())

global next_pos, board, check
next_pos = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
# alphabet : 찾을 알파벳
# x, y : 현재 좌표
def check_board(example, index, y, x):
    global check
    if index == len(example):
        check = True
        return
    # print(example[index], board[y][x])
    if board[y][x] != example[index]:
        return
    for next_y, next_x in next_pos:
        #print(">", end="")
        if 0 <= y + next_y < 5 and 0 <= x + next_x < 5:
            # print(y + next_y, x + next_x)
            check_board(example, index + 1, y + next_y, x + next_x)

for _ in range(C):
    board = []
    for _ in range(5):
        board.append(input())
    num_of_examples = int(input())
    for _ in range(num_of_examples):
        example = input()
        check = False
        for y in range(5):
            for x in range(5):
                if board[y][x] == example[0]:
                    check_board(example, 0, y, x)
                    if check:
                        print("%s YES" % example)
                        break
            if check:
                break
        if not check:
            print("%s NO" % example)