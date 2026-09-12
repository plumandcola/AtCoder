A, B, C = int(input()), int(input()), int(input())

print(3 - (A >= B) - (A >= C))
print(3 - (B >= A) - (B >= C))
print(3 - (C >= A) - (C >= B))