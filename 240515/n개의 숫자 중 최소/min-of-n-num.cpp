#include <iostream>
using namespace std;

int main() {
    int n;
    int ans = 2147483647;
    int cnt = 0;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int num;

        cin >> num;
        if (num < ans)
        {
            ans = num;
            cnt = 1;
        }
        else if (num == ans)
            cnt++;
    }
    cout << ans << " " << cnt;
    return 0;
}