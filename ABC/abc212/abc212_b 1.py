X = list(map(int, input()))

weak = False
for i in range(3):
    if X[i+1] - X[i] != 0:
        break
else:
    weak = True

for i in range(3):
    if (X[i+1] - X[i]) % 10 != 1:
        break
else:
    weak = True

if weak:
    print("Weak")
else:
    print("Strong")