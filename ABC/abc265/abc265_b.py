N, M, T = map(int, input().split())
A = list(map(int, input().split()))

bonus = [0] * (N+1) #bonus[i] := 部屋i(1 < i < N)に到達したときに増加する持ち時間
for _ in range(M):
    X, Y = map(int, input().split())
    bonus[X] = Y

for i in range(1, N): #部屋iから移動する
    if T <= A[i-1]:
        print("No")
        break
    else:
        T -= A[i-1]
        T += bonus[i+1]
else:
    print("Yes")
