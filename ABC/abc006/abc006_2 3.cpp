#include <bits/stdc++.h>
using namespace std;

int calc_a_i(vector<int>& a, int n) {
    if (a[n] == -1) a[n] = (calc_a_i(a, n-1) + calc_a_i(a, n-2) + calc_a_i(a, n-3)) % 10007;

    return a[n];
}

int main() {
    int n;
    cin >> n;
    vector<int> a(max(4, n+1), -1);
    a[1] = 0;
    a[2] = 0;
    a[3] = 1;
    
    cout << calc_a_i(a, n) << endl;
}