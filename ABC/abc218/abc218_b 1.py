P = list(map(int, input().split()))

for i in range(26):
    print(chr(P[i] + ord('a') - 1), end = "")
print() #最後の改行