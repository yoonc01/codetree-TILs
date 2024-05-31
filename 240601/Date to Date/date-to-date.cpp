#include <iostream>

using namespace std;

int m1, d1, m2, d2;
int ans = 1;

int main() {
    cin >> m1 >> d1 >> m2 >> d2;
    while(1)
    {
        if (m1 == m2 && d1 == d2)
            break;
        if (m1 == 2 && d1 == 28)
        {
            m1 = 3;
            d1 = 0;
        }
        else if (((m1 <= 6 && m1 % 2 == 0) || (m1 >= 9 && m1 % 2 == 1)) && d1 == 30)
        {
            m1 = m1 + 1;
            d1 = 0;
        }
        else if (((m1 <= 6 && m1 % 2 == 1) || (m1 >= 9 && m1 % 2 == 0)) && d1 == 31)
        {
            m1++;
            d1 = 0;
        }
        d1++;
        ans++;
    }
    cout << ans;
    return 0;
}