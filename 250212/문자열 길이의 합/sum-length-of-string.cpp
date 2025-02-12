#include <string>
#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string str;
    int n, ans = 0, countStartsWithA = 0;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> str;
        ans = ans + str.length();
        if (str[0] == 'a')
            countStartsWithA++;
    }
    cout << ans << " " << countStartsWithA;
    return 0;
}