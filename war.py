import sys
import math
import collections

card = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
def compare(a, b):
    if card.index(a) > card.index(b):
        return "1"
    elif card.index(a) < card.index(b):
        return "2"
    else:
        return False

def war(cardp_1, cardp_2, temp1, temp2):
    if len(cardp_1) < 4 or len(cardp_2) < 4:
        print("PAT")
        return 0
    temp1.extend([cardp_1.popleft(), cardp_1.popleft(), cardp_1.popleft()])
    temp2.extend([cardp_2.popleft(), cardp_2.popleft(), cardp_2.popleft()])
    a = cardp_1.popleft()
    b = cardp_2.popleft()
    temp1.append(a)
    temp2.append(b)
    if compare(a, b) == "1":
        cardp_1.extend(temp1+temp2)
        return True
    elif compare(a, b) == "2":
        cardp_2.extend(temp1+temp2)
        return True
    else:
        return war(cardp_1, cardp_2, temp1, temp2)
'''
p1, p2 뽑을 카드가 있나 확인 -> 없는 경우 게임 종료
turn +1
p1, p2의 카드 뽑아서 나온 a, b 비교
1. a가 더 크다
2. b가 더 크다
3. 무승부
    -> WAR
        # p1, p2 둘 다 카드 4개 이상 있나 확인 -> 없으면 게임 종료
        # p1, p2 둘 다 3개씩 펼친다
        # a b 비교
        # 1. a가 더 크다 -> WAR 종료
        # 2. b가 더 크다 -> WAR 종료
        # 3. 무승부
            -> WAR

종료 시 출력 코드
 if not cardp_1 and cardp_2:
        print("2 %d" % turn)
    elif cardp_1 and not cardp_2:
        print("1 %d" % turn)
    elif not cardp_1 and not cardp_2:
        print("PAT")
'''

cardp_1 = collections.deque()
cardp_2 = collections.deque()

n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1.append(input()[:-1])  # the n cards of player 1
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2.append(input()[:-1])  # the m cards of player 2

turn = 0
# To debug: print("Debug messages...", file=sys.stderr)
while True:
    if not cardp_1 and cardp_2:
        print("2 %d" % turn)
        break
    elif cardp_1 and not cardp_2:
        print("1 %d" % turn)
        break
    elif not cardp_1 and not cardp_2:
        print("PAT")
        break

    turn += 1

    a = cardp_1.popleft()
    b = cardp_2.popleft()
    if compare(a, b) == "1":
        cardp_1.extend([a, b])
    elif compare(a, b) == "2":
        cardp_2.extend([a, b])
    else:
        temp1 = [a]
        temp2 = [b]
        result = war(cardp_1, cardp_2, temp1, temp2)
        if not result:
            break