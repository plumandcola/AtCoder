N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans_1 = 0
ans_2 = 0
for i in range(N):
    for j in range(N):
        if A[i] == B[j]:
            if i == j:
                ans_1 += 1
            else:
                ans_2 += 1

print(ans_1)
print(ans_2)