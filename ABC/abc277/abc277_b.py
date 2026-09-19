import re

ans = "Yes"
cards = set()
pattern = re.compile(r"[HDCS][A2-9TJQK]")
N = int(input())
for _ in range(N):
    S = input()
    if not re.match(pattern, S):
        ans = "No"
        break
    cards.add(S)
else:
    if len(cards) != N:
        ans = "No"

print(ans)