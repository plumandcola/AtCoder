#include <bits/stdc++.h>
using namespace std;

int main() {
    string S, keyboards = "WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW";
    cin >> S;

    if (S == keyboards.substr(0, 20)) cout << "Do" << endl;
    else if (S == keyboards.substr(2, 20)) cout << "Re" << endl;
    else if (S == keyboards.substr(4, 20)) cout << "Mi" << endl;
    else if (S == keyboards.substr(5, 20)) cout << "Fa" << endl;
    else if (S == keyboards.substr(7, 20)) cout << "So" << endl;
    else if (S == keyboards.substr(9, 20)) cout << "La" << endl;
    else if (S == keyboards.substr(11, 20)) cout << "Si" << endl;
}