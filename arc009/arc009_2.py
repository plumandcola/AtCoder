b = list(map(int, input().split())) #私達が普段使用する数字 → AtCoder国の数字
b_dict = {b[i]: i for i in range(10)} #AtCoder国の数字 → 私達が普段使用する数字

N = int(input())
a = [0] * N
for i in range(N):
    for n in map(int, input()): #a_jを文字列のまま受け取り、先頭から1文字ずつint型にする
        a[i] = a[i] * 10 + b_dict[n]

a.sort()

ans = [0] * N
for i in range(N):
    for n in map(int, str(a[i])): #a[i]を文字列にして、先頭から1文字ずつint型にする
        ans[i] = ans[i] * 10 + b[n]
    print(ans[i])