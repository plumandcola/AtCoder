#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    
    cout << (char)toupper(S[0]);
    for (int i = 1; i < S.size(); i++) {
        cout << (char)tolower(S[i]);
    }
    cout << endl;
}