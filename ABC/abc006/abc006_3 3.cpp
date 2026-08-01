#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    
    int y = M % 2;
    
    if (y == 1) {
        N -= 1;
        M -= 3;
    }
    
    int x = 2 * N - M / 2;
    int z = - N + M / 2;
    
    if (x < 0 || z < 0) cout << -1 << " " << -1 << " " << -1 << endl;
    else cout << x << " " << y << " " << z << endl;
}