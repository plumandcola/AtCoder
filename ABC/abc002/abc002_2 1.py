W = input()

ans = ""
for c in W:
    if c not in "aiueo":
        ans += c

print(ans)