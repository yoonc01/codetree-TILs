#include <iostream>
using namespace std;

int main() {
    int a, b, arr[11] = {};
    int ans = 0;
    cin >> a >> b;
    while (1 < a)
    {
        arr[a % b]++;
        a = a / b;
    }
    for (int i = 0; i < b; i++)
    {
        ans = ans + arr[i] * arr[i];
    }
    cout << ans;
    return 0;
}