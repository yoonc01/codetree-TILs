#include <iostream>
using namespace std;

bool    is_369(int n)
{
    while(n)
    {
        if (n % 10 == 3 || n % 10 == 6 || n % 10 == 9)
            return (true);
        n = n / 10;
    }
    return (false);
}

bool condition(int n)
{
    return (is_369(n) || n % 3 == 0);
}

int main() {
    int a, b, cnt = 0;

    cin >> a >> b;
    for (int i = a; i < b + 1; i++)
    {
        if (condition(i))
            cnt++;
    }
    cout << cnt;
    return 0;
}