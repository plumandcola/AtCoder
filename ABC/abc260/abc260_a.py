from collections import Counter

S = Counter(input())
for c in S:
    if S[c] == 1:
        print(c)
        break
else: #Sに1度だけ含まれる文字が存在しない場合
    print(-1)
