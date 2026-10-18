#include <bits/stdc++.h>
using namespace std;

int main() {
    // 30点解法
    int N;
    cin >> N;

    vector<int> x(N), y(N);
    for (int i = 0; i < N; i++) cin >> x[i] >> y[i];

    vector<int> ans(3, 0);
    for (int i = 0; i < N-2; i++) {
        for (int j = i+1; j < N-1; j++) {
            for (int k = j+1; k < N; k++) {
                vector<int> inner_products(3);
                inner_products[0] = (x[j] - x[i]) * (x[k] - x[i]) + (y[j] - y[i]) * (y[k] - y[i]);
                inner_products[1] = (x[i] - x[j]) * (x[k] - x[j]) + (y[i] - y[j]) * (y[k] - y[j]);
                inner_products[2] = (x[i] - x[k]) * (x[j] - x[k]) + (y[i] - y[k]) * (y[j] - y[k]);

                int flag = 0;
                for (int l = 0; l < 3; l++) {
                    if (inner_products[l] < 0) flag = 2;
                    if (inner_products[l] == 0) flag = 1;
                }
                ans[flag]++;
            }
        }
    }

    cout << ans[0] << " " << ans[1] << " " << ans[2] << endl;
}