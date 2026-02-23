n = int(input())

if n >= 5:
    print("Yes")
else:
    print("Yes" if 2 ** n > n ** 2 else "No")