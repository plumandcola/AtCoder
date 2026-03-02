from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_dict = defaultdict(set)
for i in range(N):
    A_dict[A[i]].add(i)

ans_1 = 0
ans_2 = 0
for i in range(N):
    ans_1 += int(i in A_dict[B[i]])
    ans_2 += len(A_dict[B[i]]) - int(i in A_dict[B[i]])

print(ans_1)
print(ans_2)