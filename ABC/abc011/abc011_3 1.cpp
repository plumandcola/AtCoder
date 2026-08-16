#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M = 3; // Mは、選べる数字の上限
    cin >> N;
    vector<int> NG(3);
    for (int i = 0; i < 3; i++) cin >> NG[i];

    vector<int> steps(N+1, -1);
    steps[N] = 0;
    for (int i = N; i > 0; i--) {
        if (steps[i] == -1 || find(NG.begin(), NG.end(), i) != NG.end()) continue;

        for (int j = i-1; j >= max(0, i-M); j--) {
            if (steps[j] == -1 || steps[j] > steps[i]) steps[j] = steps[i] + 1;
        }
    }

    cout << (0 <= steps[0] && steps[0] <= 100 ? "YES" : "NO") << endl;
}