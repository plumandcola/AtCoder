#include <bits/stdc++.h>
using namespace std;

int main() {
    int Deg, Dis;
    cin >> Deg >> Dis;
    
    vector<string> Dirs = {"N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"};
    int i = ((Deg * 10 + 1125) / 2250) % 16;
    string Dir = Dirs[i];
    
    if (Dis < 15) Dir = "C";
    
    vector<int> Diss = {15, 93, 201, 327, 477, 645, 831, 1029, 1245, 1467, 1707, 1959};
    int W = upper_bound(Diss.begin(), Diss.end(), Dis) - Diss.begin();
    
    cout << Dir << " " << W << endl;
}