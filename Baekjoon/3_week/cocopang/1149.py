import sys
n = int(sys.stdin.readline().rstrip())
dp = [
    [sys.maxsize]*3
    for _ in range(1001)
]
array = [
    list(map(int, sys.stdin.readline().rstrip().split()))
    for _ in range(n)
]
for i in range(3):
    dp[0][i] = array[0][i]
color_box = [
    ['red', 'green', 'blue']
    for _ in range(n)
]
for i in range(1, n):
    for j in range(3):
        for z in range(3):
            if not color_box[i][j] == color_box[i-1][z]:
                dp[i][j] = min(dp[i-1][z]+array[i][j], dp[i][j])
print(min(dp[n-1]))
