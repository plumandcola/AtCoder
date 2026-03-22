H, W = map(int, input().split())
R, C = map(int, input().split())

print((R != 1) + (R != H) + (C != 1) + (C != W))