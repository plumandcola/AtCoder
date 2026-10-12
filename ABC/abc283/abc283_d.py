q = []
count = [False] * 26
for c in input():
    if c == '(':
        q.append(c)
    elif c == ')':
        while True:
            c = q.pop()
            if c == '(':
                break
            count[ord(c) - ord('a')] = False
    else:
        if count[ord(c) - ord('a')] == True:
            print("No")
            break
        q.append(c)
        count[ord(c) - ord('a')] = True
else:
    print("Yes")
