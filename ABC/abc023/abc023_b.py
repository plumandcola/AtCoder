N = int(input())
S = input()

if N % 6 == 1:
    ans = "bcabca" * (N // 6) + "b"
    if ans == S:
        K = N // 2
    else:
        K = -1
elif N % 6 == 3:
    ans = "abc" * (N // 3)
    if ans == S:
        K = N // 2
    else:
        K = -1
elif N % 6 == 5:
    ans = "cabcab" * (N // 6) + "cabca"
    if ans == S:
        K = N // 2
    else:
        K = -1
else:
    K = -1

print(K)