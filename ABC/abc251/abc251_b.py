N, W = map(int, input().split())
A = list(map(int, input().split()))

ans = [False] * W #ans[i] := i+1が良い整数かどうか

#おもりを1個使う場合
for i in range(N):
    if A[i] <= W:
        ans[A[i] - 1] = True

#おもりを2個使う場合
for i in range(N-1):
    for j in range(i+1, N):
        if A[i] + A[j] <= W:
            ans[A[i] + A[j] - 1] = True

#おもりを3個使う場合
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if A[i] + A[j] + A[k] <= W:
                ans[A[i] + A[j] + A[k] - 1] = True

print(sum(ans))