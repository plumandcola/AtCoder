m = int(input())

if m < 100: print(f"{0:02}")
elif 100 <= m <= 5000: print(f"{m // 100:02}")
elif 6000 <= m <= 30000: print(m // 1000 + 50)
elif 35000 <= m <= 70000: print(m // 5000 + 74)
elif m > 70000: print(89)