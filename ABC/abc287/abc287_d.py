S = input()
T = input()

pre = [False] * (len(T) + 1) #pre[i] := Sの先頭i文字とTの先頭i文字がマッチするかどうか
pre[0] = True
for i in range(len(T)):
    pre[i+1] = pre[i] & (S[i] == T[i] or S[i] == '?' or T[i] == '?')

suf = [False] * (len(T) + 1) #suf[i] := Sの末尾i文字とTの末尾i文字がマッチするかどうか
suf[len(T)] = True
for i in range(len(T)):
    suf[-i-2] = suf[-i-1] & (S[-i-1] == T[-i-1] or S[-i-1] == '?' or T[-i-1] == '?')

for x in range(len(T) + 1):
    print("Yes" if pre[x] and suf[x] else "No")
