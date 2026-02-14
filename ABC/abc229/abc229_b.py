A, B = map(int, input().split())

while A and B:
    if A%10 + B%10 >= 10:
        print("Hard")
        break
    
    A //= 10
    B //= 10
else:
    print("Easy")