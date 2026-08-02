N = int(input())

X_l = 1
X_r = N
while X_l != X_r:
    mid = (X_l + X_r) // 2
    print("?", X_l, mid, 1 ,N)
    T = int(input())
    if T == mid - X_l + 1:
        X_l = mid + 1
    else:
        X_r = mid

Y_l = 1
Y_r = N
while Y_l != Y_r:
    mid = (Y_l + Y_r) // 2
    print("?", 1, N, Y_l, mid)
    T = int(input())
    if T == mid - Y_l + 1:
        Y_l = mid + 1
    else:
        Y_r = mid

print("!", X_l, Y_l)