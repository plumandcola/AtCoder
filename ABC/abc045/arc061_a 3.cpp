#include <bits/stdc++.h>
using namespace std;

vector<vector<long long>> matrix_product(vector<vector<long long>> A, vector<vector<long long>> B) {
    long long m = A.size();
    long long n = B.size();
    long long l = B[0].size();
    vector<vector<long long>> AB(m, vector<long long>(l, 0));
    for (long long i = 0; i < m; i++) {
        for (long long j = 0; j < l; j++) {
            for (long long k = 0; k < n; k++) {
                AB[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    return AB;
}

int main() {
    string S;
    cin >> S;

    vector<vector<long long>> ans = {{0}, {S[0] - '0'}, {1}};
    for (long long i = 1; i < S.size(); i++) {
        ans = matrix_product({{2, 1, 0}, {0, 10, 2 * (S[i] - '0')}, {0, 0, 2}}, ans);
    }
    ans = matrix_product({{1, 1, 0}}, ans);

    cout << ans[0][0] << endl;
}