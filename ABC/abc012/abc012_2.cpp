#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    int h = N / 3600;
    int m = (N / 60) % 60;
    int s = N % 60;

    cout << format("{:02}:{:02}:{:02}", h, m, s);
}