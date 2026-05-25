N, K, Q = map(int, input().split())
A = list(map(int, input().split()))

for L in map(int, input().split()):
    #左からL番目のコマが一番右のマスにあるならば
    if A[L-1] == N:
        #何も行わない
        continue
    
    #左からL番目のコマがあるマスの1つ右のマスにコマが無いならば
    elif L == K or A[L] != A[L-1] + 1:
        #左からL番目のコマを1つ右のマスに移動させる
        A[L-1] += 1

print(*A)