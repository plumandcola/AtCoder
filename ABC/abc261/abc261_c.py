count = {}

N = int(input())
for _ in range(N):
    S = input()

    # S_1,…,S_{i−1}の中にS_iと同じ文字列が存在しない場合
    if S not in count:
        print(S)
        count[S] = 1
    
    # S_1,…,S_{i−1}の中にS_iと同じ文字列が存在する場合
    else:
        print(S, "(", count[S], ")", sep="")
        count[S] += 1
