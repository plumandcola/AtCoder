X = list(map(int, input())) #Xを1文字ずつint型にしたlistに

n = len(X)
s = [0] * (n+1) #累積和
for i in range(n):
    s[i+1] = s[i] + X[i]

ans = "" #下の位から
m = 0
for i in range(n, 0, -1):
    m += s[i]
    ans += str(m % 10)
    m //= 10

while m: #繰り上がりが残っている場合
    ans += str(m % 10)
    m //= 10

print(ans[::-1]) #逆にするのを忘れない