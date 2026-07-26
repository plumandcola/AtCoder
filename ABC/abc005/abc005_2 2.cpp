#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> T(N);
    for (int i = 0; i < N; i++) cin >> T[i];
    
    sort(T.begin(), T.end());
    
    cout << T[0] << endl;
}