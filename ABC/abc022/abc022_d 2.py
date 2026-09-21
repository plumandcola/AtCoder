#100点解法
def calc_diff_diff(A: list[int], N: int) -> int:
    """Σ_(i<j) (A_i - A_j) ** 2"""
    return N * sum(A[i] ** 2 for i in range(N)) - sum(A) ** 2


N = int(input())

Ax = [0] * N
Ay = [0] * N
for i in range(N):
    Ax[i], Ay[i] = map(int, input().split())

Bx = [0] * N
By = [0] * N
for i in range(N):
    Bx[i], By[i] = map(int, input().split())

print(((calc_diff_diff(Bx, N) + calc_diff_diff(By, N)) / (calc_diff_diff(Ax, N) + calc_diff_diff(Ay, N))) ** 0.5)