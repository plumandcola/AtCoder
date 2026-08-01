#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> a(n);
    if (n >= 3) {
        a[2] = 1;
        for (int i = 0; i < n-3; i++) {
            a[i+3] = (a[i] + a[i+1] + a[i+2]) % 10007;
        }
    }
    
    cout << a[n-1] << endl;
}