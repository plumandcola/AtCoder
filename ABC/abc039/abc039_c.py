S = input()

keyboards = "WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW"

if S == keyboards[:20]:
    print("Do")
elif S == keyboards[2:22]:
    print("Re")
elif S == keyboards[4:24]:
    print("Mi")
elif S == keyboards[5:25]:
    print("Fa")
elif S == keyboards[7:27]:
    print("So")
elif S == keyboards[9:29]:
    print("La")
elif S == keyboards[11:31]:
    print("Si")
