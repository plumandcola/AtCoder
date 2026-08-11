#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, a;
    cin >> N;
    
    set<int> A;
    for (int i = 0; i < N; i++) {
        cin >> a;
        A.insert(a);
    }

    auto it = A.end();
    it--;
    it--;
    
    cout << *it << endl;
}