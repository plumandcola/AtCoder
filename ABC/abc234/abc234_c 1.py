K = int(input())

ans = "" #逆から順に
while K:
    if K & 1 == 0:
        ans += "0"
    else:
        ans += "2"
    K >>= 1

print(ans[::-1])