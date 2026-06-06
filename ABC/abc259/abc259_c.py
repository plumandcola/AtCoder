def rle(S: str) -> list[tuple[str, int]]:
    s = []
    n = len(S)
    l = 0
    r = 0
    while l < n:
        while r < n and S[l] == S[r]:
            r += 1
        s.append((S[l], r - l))
        l = r
    return s


S = input()
T = input()

s = rle(S)
t = rle(T)

ans = "Yes"

#文字列の構成が違う場合
if len(s) != len(t):
    ans = "No"

i = 0
while i < len(s) and i < len(t):
    #文字が違う場合
    if s[i][0] != t[i][0]:
        ans = "No"
        break

    #Sの文字数の方が多い場合
    if s[i][1] > t[i][1]:
        ans = "No"
        break

    #Sの方が1文字なために挿入できない場合
    if s[i][1] == 1 and t[i][1] >= 2:
        ans = "No"
        break

    i += 1

print(ans)