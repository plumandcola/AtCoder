A, B = map(int, input().split())

n = (A + 2000 * B) // (2 * A)

print(f"{n//1000}.{n%1000:03}")