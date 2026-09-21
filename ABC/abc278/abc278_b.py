H, M = map(int, input().split())

while True:
    if 0 <= H//10 * 10 + M//10 <= 23 and 0 <= H%10 * 10 + M%10 <= 59:
        break

    M += 1
    if M == 60:
        H += 1
        M = 0
        if H == 24:
            H = 0

print(H, M)