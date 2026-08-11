#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, A, first = 0, second = -1; // 最も高い金額、2番目に高い金額
    cin >> N;
    
    for (int i = 0; i < N; i++) {
        cin >> A;
        if (A > first) {
            second = first;
            first = A;
        } else if (first > A && A > second) {
            second = A;
        }
    }
    
    cout << second << endl;
}