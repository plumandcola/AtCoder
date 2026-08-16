#include <bits/stdc++.h>
using namespace std;

vector<vector<unsigned int>> matrix_product(vector<vector<unsigned int>> A, vector<vector<unsigned int>> B) {
    unsigned int m = A.size();
    unsigned int n = B.size();
    unsigned int l = B[0].size();
    vector<vector<unsigned int>> AB(m, vector<unsigned int>(l, 0));
    for (unsigned int i = 0; i < m; i++) {
        for (unsigned int j = 0; j < l; j++) {
            for (unsigned int k = 0; k < n; k++) {
                AB[i][j] ^= A[i][k] & B[k][j];
            }
        }
    }
    return AB;
}

int main() {
    unsigned int K, M;
    cin >> K >> M;

    vector<unsigned int> A(K), C(K);
    for (unsigned int i = 0; i < K; i++) cin >> A[i];
    for (unsigned int i = 0; i < K; i++) cin >> C[i];
    
    if (M <= K) {
        cout << A[M-1] << endl;
        return 0;
    }
    
    vector<vector<unsigned int>> ans(K, vector<unsigned int>(1));
    for (unsigned int i = 0; i < K; i++) {
        ans[i][0] = A[K-i-1];
    }
    unsigned int mask = UINT32_MAX;
    vector<vector<unsigned int>> transformation_matrix(K, vector<unsigned int>(K, 0));
    for (int j = 0; j < K; j++) {
        transformation_matrix[0][j] = C[j];
    }
    for (int i = 1; i < K; i++) {
        transformation_matrix[i][i-1] = mask;
    }

    M -= K;
    
    while (M) {
        if ((M & 1) == 1) {
            ans = matrix_product(transformation_matrix, ans);
        }
        transformation_matrix = matrix_product(transformation_matrix, transformation_matrix);
        M >>= 1;
    }
    
    cout << ans[0][0] << endl;
}