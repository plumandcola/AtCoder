def is_leap_year(Y: int) -> bool:
    if Y % 400 == 0:
        return True
    elif Y % 100 == 0:
        return False
    elif Y % 4 == 0:
        return True
    else:
        return False


Y, M, D = map(int, input().split('/'))

M_to_D = [[-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
          [-1, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]

while Y % (M*D) != 0:
    D += 1
    if D > M_to_D[is_leap_year(Y)][M]:
        M += 1
        D = 1
    if M == 13:
        Y += 1
        M = 1

print(f"{Y:04}/{M:02}/{D:02}")