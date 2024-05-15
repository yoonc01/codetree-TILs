#include <iostream>
#include <climits>
#include <algorithm>
using namespace std;

int main() {
    int ans = 0;
    for (int i = 0; i < 10; i++)
    {
        int n;
        cin >> n;
        ans = max(ans, n);
    }
    cout << ans;
    return 0;
}