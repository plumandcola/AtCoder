N = int(input())
A = list(map(int, input().split()))
B = {b: i for i, b in enumerate(map(int, input().split()))}

ans_1 = 0
ans_2 = 0
for i in range(N):
    if A[i] in B:
        if B[A[i]] == i:
            ans_1 += 1
        else:
            ans_2 += 1

print(ans_1)
print(ans_2)