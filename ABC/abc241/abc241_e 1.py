N, K = map(int, input().split())
A = list(map(int, input().split()))

s = [0]
i = 0
index = [-1] * N #index[i] := アメの個数の余りがはじめてiになるまでの回数
index[0] = 0
r = 0 #今のアメの個数の余り
while True:
    i += 1
    s.append(s[-1] + A[r])

    r = s[-1] % N
    if index[r] != -1: #アメの個数の余りがrになったタイミングがある = 1周した
        break
    index[r] = i

cycle = i - index[r] #1周期の長さ

if K <= index[r]: #周期に入る前に終わる場合
    print(s[K])
else:
    ans = 0
    ans += s[index[r]] #周期に入るまでの個数
    ans += (K - index[r]) // cycle * (s[i] - s[index[r]]) #周期中での個数
    ans += s[(K - index[r]) % cycle + index[r]] - s[index[r]] #最後に周期からはみ出たところの個数
    print(ans)
