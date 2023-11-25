#include <iostream>
#include <string>
using namespace std;

int main() {
    string str, to_find;
    int ans;

    cin >> str >> to_find;
    ans = str.find(to_find);
    if (ans == string::npos)
        cout << -1;
    else
        cout << ans;
    return 0;
}