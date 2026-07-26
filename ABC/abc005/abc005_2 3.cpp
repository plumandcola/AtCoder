#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> T(N);
    for (int i = 0; i < N; i++) cin >> T[i];
    
    cout << *min_element(T.begin(), T.end()) << endl;
}