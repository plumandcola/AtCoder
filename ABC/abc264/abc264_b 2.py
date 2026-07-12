R, C = map(int, input().split())

print(["white", "black"][min(min(R, 16 - R), min(C, 16 - C)) % 2])