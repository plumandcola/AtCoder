#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> nums(3);
    for (int i = 0; i < 3; i++) cin >> nums[i];

    sort(nums.begin(), nums.end());

    if (nums[0] == 5 && nums[1] == 5 && nums[2] == 7) cout << "YES" << endl;
    else cout << "NO" << endl;
}