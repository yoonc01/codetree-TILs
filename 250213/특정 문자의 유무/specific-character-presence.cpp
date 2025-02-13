#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string str;
    cin >> str;

    string ee = (str.find("ee") != string::npos) ? "Yes" : "No";
    string ab = (str.find("ab") != string::npos) ? "Yes" : "No";

    cout << ee << " " << ab << "\n";
    return 0;
}
