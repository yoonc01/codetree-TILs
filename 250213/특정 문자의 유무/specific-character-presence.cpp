#include <string>
#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string str;
    string ans = "";
    cin >> str;

    if (str.find("ee") != string::npos) {
        ans.append("Yes ");
    } else {
        ans.append("No ");
    }
    if (str.find("ab") != string::npos) {
        ans.append("Yes ");
    } else {
        ans.append("No ");
    }
    cout << ans;
    return 0;
}