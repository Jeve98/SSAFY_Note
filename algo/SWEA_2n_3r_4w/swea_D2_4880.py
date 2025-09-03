# 1: 가위, 2: 바위, 3: 보
def battle(start, end):
    if start == end:
        return start
    else:
        left = battle(start, (start + end) // 2)
        right = battle((start + end) // 2 + 1, end)

        if win(card[left], card[right]):
            return left
        else:
            return right


# True : left win, False : right win
def win(left, right):
    # 무승부
    if left == right:
        return True
    elif (left == 1 and right == 3) or (left == 2 and right == 1) or (left == 3 and right == 2):
        return True
    else:
        return False


T = int(input())
for case in range(T):
    people = int(input())
    card = list(map(int, input().split()))

    winner = battle(0, people - 1) + 1

    print(f'#{case + 1} {winner}')
