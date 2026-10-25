#include <bits/stdc++.h>
using namespace std;

int main() {
    int W, H;
    cin >> W >> H;

    if (W / 4 == H / 3) cout << "4:3" << endl;
    else if (W / 16 == H / 9) cout << "16:9" << endl;
}