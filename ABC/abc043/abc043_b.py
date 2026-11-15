ans = []
for s in input():
    if s == '0' or s == '1':
        ans.append(s)
    elif s == 'B' and ans:
        ans.pop()

print("".join(ans))