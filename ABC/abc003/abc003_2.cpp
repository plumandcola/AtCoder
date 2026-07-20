#include <bits/stdc++.h>
using namespace std;

int main() {
    string S, T, atcoder = "atcoder";
    cin >> S >> T;
    
    bool ans = true;
    for (int i = 0; i < S.size(); i++) {
        if (S[i] != T[i]) {
            if (S[i] == '@' && atcoder.find(T[i]) == string::npos) ans = false;
            else if (T[i] == '@' && atcoder.find(S[i]) == string::npos) ans = false;
            else if (S[i] != '@' && T[i] != '@') ans = false;
        }
    }
    
    cout << (ans ? "You can win" : "You will lose") << endl;
}