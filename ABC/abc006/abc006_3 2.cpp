#include <bits/stdc++.h>
using namespace std;

int main() {
    // 30点解法のはずが、満点を取れてしまう
    int N, M;
    cin >> N >> M;
    
    for (int x = 0; x <= N; x++) {
        for (int y = 0; y <= N-x; y++) {
            int z = N - x - y;
            if (2 * x + 3 * y + 4 * z == M) { // z >= 0であることは、y < N-x+1から保証されている
                cout << x << " " << y << " " << z << endl;
                return 0;
            }
        }
    }
    
    cout << -1 << " " << -1 << " " << -1 << endl;
}