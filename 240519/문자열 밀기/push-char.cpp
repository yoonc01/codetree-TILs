#include <iostream>
#include <string>
using namespace std;

int main() {
    string str, ans = "";
    cin >> str;
    int len = str.length();
    for (int i = 1; i < len; i++)
        ans = ans + str[i];
    ans = ans + str[0];
    cout << ans;
    return 0;
}