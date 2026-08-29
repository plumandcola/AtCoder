#100点解法
n = int(input())

#いもす法
s = [0] * 1000002
for _ in range(n):
    a, b = map(int, input().split())
    s[a] += 1
    s[b+1] -= 1

ans = 0 #最も人気のある濃さの色
for i in range(1000001):
    if s[i] >= s[ans]:
        ans = i
    s[i+1] += s[i]

print(s[ans])