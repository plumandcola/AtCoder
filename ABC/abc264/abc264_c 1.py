import itertools

H_1, W_1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H_1)]

H_2, W_2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H_2)]

ans = "No"
for h in itertools.combinations(range(H_1), H_2):
    for w in itertools.combinations(range(W_1), W_2):
        ans_i = True
        for i in range(H_2):
            for j in range(W_2):
                if A[h[i]][w[j]] != B[i][j]:
                    ans_i = False
        if ans_i == True:
            ans = "Yes"

print(ans)