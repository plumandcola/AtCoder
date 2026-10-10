N = int(input())

s = "abc"

for i in range(3 ** N):
    for j in range(N-1, -1, -1):
        c = chr(ord('a') + i // (3 ** j) % 3)
        print(c, end="")
    print() #改行
