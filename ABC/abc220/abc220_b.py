def base_k_to_ten(N: str, k: int) -> int:
    """K進法で表された文字列Nを、10進法の整数に変換する"""
    result = 0
    for n in map(int, N):
        result = result * k + n
    return result


K = int(input())
A, B = input().split()

print(base_k_to_ten(A, K) * base_k_to_ten(B, K))