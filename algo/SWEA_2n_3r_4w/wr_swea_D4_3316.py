# bit-masking
# import sys
# sys.stdin = open('../input.txt', 'r')

T = int(input())
for case in range(T):
    managerList = input()

    dp = [[0] * 16 for _ in range(len(managerList) + 1)]     # dp[day][출근자_bitmask]
    dp[0][1] = 1    # 0 번째 날의 출근자(열쇠 소지자)는 A

    for day in range(1, len(managerList) + 1):
        # bit-masking
        todayManager = 1 << (ord(managerList[day - 1]) - ord('A'))

        # A: 0001, B: 0010, C: 0100, D: 1000
        # 전원 출근시, A | B | C | D == 1111 (15)
        for participate in range(1, 16):
            # 이번 조합에 오늘의 매니저가 포함되어 있는 경우
            if participate & todayManager:
                for prePar in range(1, 16):
                    # 어제를 기준으로 가능했던 조합 중, 이번 조합에 포함된 인원이 있을 경우
                    if dp[day - 1][prePar] != 0 and prePar & participate:
                        # 오늘 해당 조합은 가능 (경우의 수 누적)
                        dp[day][participate] += dp[day - 1][prePar]
                        dp[day][participate] %= 1000000007

    # 마지막 날의 모든 경우의 수의 합
    ans = sum(dp[len(managerList)]) % 1000000007

    print(f'#{case + 1} {ans}')
