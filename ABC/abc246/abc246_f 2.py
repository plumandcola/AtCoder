import itertools

N, L = map(int, input().split())
S = [set(input()) for _ in range(N)]

ans = 0
for i in range(1, N+1):
    for comb in itertools.combinations(S, i): #Sの中からi個選ぶ組み合わせ
        count = 0 #comb全てに含まれる文字をカウント
        for c in "abcdefghijklmnopqrstuvwxyz": #全ての英小文字を調べる
            count += all(c in s for s in comb) #comb全てに含まれていればcountに足す
        if i & 1 == 1:
            ans = (ans + pow(count, L, 998244353)) % 998244353
        elif i & 1 == 0:
            ans = (ans - pow(count, L, 998244353)) % 998244353

print(ans)