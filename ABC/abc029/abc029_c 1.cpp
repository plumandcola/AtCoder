#include <bits/stdc++.h>
using namespace std;

void dfs(string s, int N) {
    if (N == 0) {
        cout << s << endl;
        return;
    }

    for (char c = 'a'; c <= 'c'; c++) {
        dfs(s + c, N - 1);
    }
}

int main() {
    int N;
    cin >> N;
    
    dfs("", N);
}