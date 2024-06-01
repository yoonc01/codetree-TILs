#include <iostream>

using namespace std;

int days_of_month[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
int m1, d1, m2, d2;

int total_days(int m, int d)
{
    int ans = 0;
    for (int i = 0; i < m; i++)
    {
        ans = ans + days_of_month[i];
    }
    ans = ans + d;
    return (ans);
}
int main() {

    cin >> m1 >> d1 >> m2 >> d2;
    
    cout << total_days(m2, d2) - total_days(m1, d1) + 1;
    return 0;
}