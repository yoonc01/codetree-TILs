#include <iostream>

int days_of_month[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
int m1, m2, d1, d2;

using namespace std;

int total_days(int m, int d)
{
    int days = 0;

    for (int i = 0; i < m; i++)
    {
        days = days + days_of_month[i];
    }
    return (days + d);
}

int main() {
    cin >> m1 >> d1 >> m2 >> d2;

    int diff = total_days(m2, d2) - total_days(m1, d1);

    if (diff >= 0)
    {
        if (diff % 7 == 0)
            cout << "Mon";
        else if (diff % 7 == 1)
            cout << "Tue";
        else if (diff % 7 == 2)
            cout << "Wed";
        else if (diff % 7 == 3)
            cout << "Thu";
        else if (diff % 7 == 4)
            cout << "Fri";
        else if (diff % 7 == 5)
            cout << "Sat";
        else
            cout << "Sun";
    }
    else
    {
        if (diff % 7 == 0)
            cout << "Mon";
        else if (diff % 7 == -1)
            cout << "Sun";
        else if (diff % 7 == -2)
            cout << "Sat";
        else if (diff % 7 == -3)
            cout << "Fri";
        else if (diff % 7 == -4)
            cout << "Thu";
        else if (diff % 7 == -5)
            cout << "Wed";
        else
            cout << "Tue";
    }
    return 0;
}