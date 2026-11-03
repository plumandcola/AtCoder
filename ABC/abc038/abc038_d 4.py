#100点解法
import bisect

N = int(input())
boxes = [] #wの昇順かつhの降順でソート
for _ in range(N):
    w, h = map(int, input().split())
    boxes.append((w, -h))
boxes.sort()

dp = []
for w, h in boxes:
    h *= -1 #hの符号を反転させているので、元に戻す
    j = bisect.bisect_left(dp, h)
    if j == len(dp):
        dp.append(h)
    else:
        dp[j] = h

print(len(dp))