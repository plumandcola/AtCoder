#include <bits/stdc++.h>
using namespace std;

int main() {
    // 10点解法のはずが、30点取れてしまう
    int N, M;
    cin >> N >> M;
    
    for (int x = 0; x <= N; x++) {
        for (int y = 0; y <= N; y++) {
            for (int z = 0; z <= N; z++) {
                if (x + y + z == N && 2 * x + 3 * y + 4 * z == M) {
                    cout << x << " " << y << " " << z << endl;
                    return 0;
                }
            }
        }
    }
    
    cout << -1 << " " << -1 << " " << -1 << endl;
}