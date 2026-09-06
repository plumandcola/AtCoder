X = input()

X = X.replace("ch", "").replace("o", "").replace("k", "").replace("u", "")

if X == "":
    print("YES")
else:
    print("NO")
