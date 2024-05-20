#include <iostream>
#include <string>
using namespace std;

int main() {
    int n, ans = 0;
    string a, str;

    cin >> n;
    cin >> a;
    for (int i = 0; i < n; i++)
    {
        cin >> str;
        if (a == str)
            ans++;
    }
    cout << ans;
    return 0;
}