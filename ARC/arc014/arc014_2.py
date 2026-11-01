N = int(input())
W = [input() for _ in range(N)]

Ws = {W[0]}
for i in range(1, N):
    if W[i][0] != W[i-1][-1] or W[i] in Ws:
        if i % 2 == 1:
            print("WIN")
        elif i % 2 == 0:
            print("LOSE")
        break
    
    Ws.add(W[i])
else:
    print("DRAW")
