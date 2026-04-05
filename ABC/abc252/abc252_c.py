N = int(input())
S = [input() for _ in range(N)]

count = [[0] * 10 for _ in range(10)]
"""count[i][t] := 数字iを、T%10=tで止めなければならないリールの数"""

for s in S:
    for t in range(10):
        count[int(s[t])][t] += 1

ans = float("inf")
for i in range(10): #数字0〜9について、目標を達成するのに必要な最小の時間を求める
    ans_i = 0 #数字0〜9について、目標を達成するのに必要な最小の時間
    for t in range(10):
        ans_i = max(ans_i, (count[i][t] - 1) * 10 + t)
    
    ans = min(ans, ans_i)

print(ans)