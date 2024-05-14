#include <iostream>
using namespace std;

int main() {
    int n;
    int cnt;

    cin >> n;
    cnt = 0;
    while(1)
    {
        if (n == 1)
            break;
        if (n % 2 == 0)
        {
            n = n / 2;
        }
        else
        {
            n = 3 * n + 1;
        }
        cnt++;
    }
    cout << cnt;
    return 0;
}