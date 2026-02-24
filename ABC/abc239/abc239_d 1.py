is_prime = [True] * 201
is_prime[0] = False #0は素数じゃない
is_prime[1] = False #1は素数じゃない
for n in range(2, 201):
    if is_prime[n]: #nが素数なら
        for i in range(2*n, 201, n):
            is_prime[i] = False

A, B, C, D = map(int, input().split())

for i in range(A, B+1):
    for j in range(C, D+1):
        if is_prime[i+j]: #青木くんが勝てる
            break
    else: #青木くんは勝てない
        print("Takahashi")
        break
else: #高橋君が勝つ方法がない
    print("Aoki")