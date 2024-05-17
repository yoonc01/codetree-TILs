#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    int cnt1 = 0, cnt2 = 0;
    cin >> str;
    for (int i = 0; i < str.length() - 1; i++)
    {
        if (str.substr(i, 2) == "ee")
            cnt1++;
        else if (str.substr(i, 2) == "eb")
            cnt2++;
    }
    cout << cnt1 << " " << cnt2;
    return 0;
}