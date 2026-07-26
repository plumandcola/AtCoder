#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, T, ans = 101;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> T;
        if (T < ans) ans = T;
    }
    
    cout << ans << endl;
}