c = {} #(n, r) -> nCr

def calc_c(n, r):
    if r < 0 or r > n:
        return 0
    
    if r == 0 or r == n:
        return 1
    
    if (n, r) not in c:
        c[(n, r)] = (calc_c(n-1, r-1) + calc_c(n-1, r))
    
    return c[(n, r)]


#100点解法
N = int(input())
C = [int(input()) for _ in range(N)]

count = [0] * N
"""count[i] := C[j](0≤j<N,j≠i)のうち、C[i]の約数の個数"""
for i in range(N):
    for j in range(N): #C[j]がC[i]の約数かどうかを調べる
        if C[i] % C[j] == 0 and i != j:
            count[i] += 1

ans = 0
for i in range(N): #C[i]のコインが最後に表を向いている確率を調べる
    for m in range(0, N, 2): #C[i]のコインの左に、C[i]の約数が書かれているコインがm枚(0≤m<N,m%2==0)ある確率を調べる
        for j in range(N): #C[i]のコインが左からj+1枚目の時を調べる
            ans += calc_c(j, m) * calc_c(N - j - 1, count[i] - m) / calc_c(N - 1, count[i]) / N

print(ans)