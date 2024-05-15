#include <iostream>
using namespace std;

int main() {
    int arr[1001] = {};
    int n, ans = -1;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        arr[num]++;
    }
    for (int i = 1; i < 1001; i++)
    {
        if (arr[i] == 1 && i > ans)
            ans = i;
    }
    cout << ans;
    return 0;
}