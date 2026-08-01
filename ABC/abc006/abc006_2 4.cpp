#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> matrix_product(vector<vector<int>> A, vector<vector<int>> B) {
    int m = A.size();
    int n = B.size();
    int l = B[0].size();
    vector<vector<int>> AB(m, vector<int>(l, 0));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < l; j++) {
            for (int k = 0; k < n; k++) {
                AB[i][j] = (AB[i][j] + A[i][k] * B[k][j]) % 10007;
            }
        }
    }
    return AB;
}

int main() {
    int n;
    cin >> n;
    
    if (n < 3) {
        cout << 0 << endl;
        return 0;
    }
    
    n -= 3;
    vector<vector<int>> a = {{1}, {0}, {0}};
    vector<vector<int>> transformation_matrix = {{1, 1, 1}, {1, 0, 0}, {0, 1, 0}};
    
    while (n) {
        if ((n & 1) == 1) {
            a = matrix_product(transformation_matrix, a);
        }
        transformation_matrix = matrix_product(transformation_matrix, transformation_matrix);
        n >>= 1;
    }
    
    cout << a[0][0] << endl;
}