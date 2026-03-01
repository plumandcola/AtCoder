S = input()

Q = int(input())
for _ in range(Q):
    t, k = map(int, input().split())
    count = 0
    k -= 1
    while t and k:
        count += 1 + k % 2
        t -= 1
        k >>= 1
    
    count = (count + ord(S[k]) - ord('A') + t) % 3 + ord('A')
    
    print(chr(count))