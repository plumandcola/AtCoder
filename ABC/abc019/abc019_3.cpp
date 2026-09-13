#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, a;
    cin >> N;
    unordered_set<int> nums;
    for (int i = 0; i < N; i++) {
        cin >> a;
        while (a % 2 == 0) a /= 2;
        nums.insert(a);
    }

    cout << nums.size() << endl;
}