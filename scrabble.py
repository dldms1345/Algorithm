import sys
import math
global points, letters
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
dictionary = [input() for i in range(n)]
letters = list(input())

points = {'e':1, 'a':1, 'i':1, 'o':1, 'n':1, 'r':1, 't':1, 'l':1, 's':1, 'u':1, 
            'd':2, 'g':2, 'b':3, 'c':3, 'm':3, 'p':3, 'f':4, 'h':4, 'v':4, 'w':4,
            'y':4, 'k':5, 'j':8, 'x':8, 'q':10, 'z':10}

def scoring_word(word):
    score = 0
    for ch in word:
        score += points.get(ch)
    return score

def is_valid_word(word):
    letter = letters.copy()
    for ch in word:
        if ch in letter:
            letter.remove(ch)
        else:
            return False
    return True
max_score = -1
answer = ""
for word in dictionary:
    if is_valid_word(word):
        tmp = scoring_word(word)
        if tmp > max_score:
            max_score = tmp
            answer = word
print(answer)
# 사전 돌면서 이 단어 letters로 만들수 있는지 판별, 만들 수 있으면 점수 매겨서 최고값이랑 비교, 최고값이면 저장 아니면 버림
# 판별법 : 첫 철자부터 확인
# To debug: print("Debug messages...", file=sys.stderr)
