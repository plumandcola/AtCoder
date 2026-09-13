s = input()
n = len(s)

l = 0
r = 0
while l < n:
    while r < n and s[l] == s[r]:
        r += 1
    print(s[l], r - l, sep="", end="")
    l = r

print() #最後の改行