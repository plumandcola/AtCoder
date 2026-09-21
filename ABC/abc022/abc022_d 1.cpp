#include <bits/stdc++.h>
using namespace std;

int main() {
    // 50点解法
    int N;
    cin >> N;
    vector<long long> Ax(N), Ay(N), Bx(N), By(N);
    for (int i = 0; i < N; i++) cin >> Ax[i] >> Ay[i];
    for (int i = 0; i < N; i++) cin >> Bx[i] >> By[i];
    
    long double s1 = 0, s2 = 0;
    for (int i = 0; i < N-1; i++) {
        for (int j = i; j < N; j++) {
            s1 += (Ax[i] - Ax[j]) * (Ax[i] - Ax[j]) + (Ay[i] - Ay[j]) * (Ay[i] - Ay[j]);
            s2 += (Bx[i] - Bx[j]) * (Bx[i] - Bx[j]) + (By[i] - By[j]) * (By[i] - By[j]);
        }
    }
    
    cout << fixed << setprecision(15) << sqrt(s2 / s1) << endl;
}