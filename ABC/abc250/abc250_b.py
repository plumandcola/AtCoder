N, A, B = map(int, input().split())

for i in range(N*A):
    for j in range(N*B):
        print("." if (i // A + j // B) % 2 == 0 else "#", end = "")
    print() #改行