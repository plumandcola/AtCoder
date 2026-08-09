#100点解法
N = int(input())
C = [int(input()) for _ in range(N)]

ans = 0
for i in range(N): #C[i]のコインが最後に表を向いている確率を調べる
    count = 0 #C[j](0≤j<N,j≠i)のうち、C[i]の約数の個数
    for j in range(N): #C[j]がC[i]の約数かどうかを調べる
        if C[i] % C[j] == 0 and i != j:
            count += 1
    ans += (count // 2 + 1) / (count + 1)

print(ans)