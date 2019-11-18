# https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1

import sys
import math
import random
# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
crr_pos = [int(i) for i in input().split()]
bomb_range = [[0,w-1], [0, h-1]]
# game loop
while True:
    bomb_dir = input()
    if bomb_dir == 'U':
        bomb_range[1][1] = crr_pos[1]-1
    elif bomb_dir == 'UR':
        bomb_range[1][1] = crr_pos[1]-1
        bomb_range[0][0] = crr_pos[0]+1
    elif bomb_dir == 'UL':
        bomb_range[0][1] = crr_pos[0]-1
        bomb_range[1][1] = crr_pos[1]-1
    elif bomb_dir == 'R':
        bomb_range[0][0] = crr_pos[0]+1
    elif bomb_dir == 'L':
        bomb_range[0][1] = crr_pos[0]-1
    elif bomb_dir == 'D':
        bomb_range[1][0] = crr_pos[1]+1
    elif bomb_dir == 'DR':
        bomb_range[0][0] = crr_pos[0]+1
        bomb_range[1][0] = crr_pos[1]+1
    elif bomb_dir == 'DL':
        bomb_range[0][1] = crr_pos[0]-1
        bomb_range[1][0] = crr_pos[1]+1
    crr_pos = [(bomb_range[0][0]+bomb_range[0][1])//2, (bomb_range[1][0]+bomb_range[1][1])//2]
    print(*crr_pos)