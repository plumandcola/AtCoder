import re

print("Yes" if re.fullmatch(r"[A-Z][1-9][0-9]{5}[A-Z]", input()) else "No")