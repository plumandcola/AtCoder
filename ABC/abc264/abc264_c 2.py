H_1, W_1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H_1)]

H_2, W_2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H_2)]

ans = "No"
for b_1 in range(1 << H_1):
    for b_2 in range(1 << W_1):
        C = []
        for i in range(H_1):
            if (b_1 >> i) & 1 == 1:
                C.append([])
                for j in range(W_1):
                    if (b_2 >> j) & 1 == 1:
                        C[-1].append(A[i][j])
        if C == B:
            ans = "Yes"

print(ans)