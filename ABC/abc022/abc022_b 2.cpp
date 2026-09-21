#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, A;
    cin >> N;

    set<int> flowers;
    for (int i = 0; i < N; i++) {
        cin >> A;
        flowers.insert(A);
    }

    cout << N - flowers.size() << endl;
}