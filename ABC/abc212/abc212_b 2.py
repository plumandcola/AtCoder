X = list(map(int, input()))
print("Weak" if all(X[i+1] - X[i] == 0 for i in range(3)) or all((X[i+1] - X[i]) % 10 == 1 for i in range(3)) else "Strong")