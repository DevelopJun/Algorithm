t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    m = int(input())
    dp = [0 for i in range(m + 1)]
    dp[0] = 1
    for t in l:
        for x in range(1, m + 1):
            if x - t >= 0:
                dp[x] += dp[x-t]

print(dp[m])
