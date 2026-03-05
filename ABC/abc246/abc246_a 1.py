x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())
x_3, y_3 = map(int, input().split())

if x_1 == x_2: x_ans = x_3
elif x_2 == x_3: x_ans = x_1
elif x_3 == x_1: x_ans = x_2

if y_1 == y_2: y_ans = y_3
elif y_2 == y_3: y_ans = y_1
elif y_3 == y_1: y_ans = y_2

print(x_ans, y_ans)