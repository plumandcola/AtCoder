X = list(map(int, input().split('.')))

print(X[0] + 1 if X[1] >= 500 else X[0])