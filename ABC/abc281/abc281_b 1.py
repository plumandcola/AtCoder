def is_satisfied(S: str) -> bool:
    if len(S) != 8: return False
    if ord(S[0]) < ord('A') or ord('Z') < ord(S[0]): return False
    if ord(S[1]) < ord('1') or ord('9') < ord(S[1]): return False
    for i in range(2, 7):
        if ord(S[i]) < ord('0') or ord('9') < ord(S[i]): return False
    if ord(S[7]) < ord('A') or ord('Z') < ord(S[7]): return False
    return True


print("Yes" if is_satisfied(input()) else "No")