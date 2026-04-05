N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

M = max(A) #おいしさの最大値

for b in B:
    if A[b-1] == M: #b番目の食品が、おいしさが最大の食品であるなら
        print("Yes")
        break
else: #ループを回り切った = 嫌いな食品が、どれもおいしさが最大の食品でない
    print("No")