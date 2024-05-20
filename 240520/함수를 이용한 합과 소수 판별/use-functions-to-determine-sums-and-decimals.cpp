#include <iostream>
using namespace std;

bool even(int n)
{
    int total = 0;
    while(n)
    {
        total = total + n % 10;
        n = n / 10;
    }
    return (total % 2 == 0);
}

bool is_prime(int n)
{
    for (int i = 2; i < n; i++)
        if (n % i == 0)
            return (false);
    return (true);
}

int main() {
    int a, b, cnt = 0;

    cin >> a >> b;
    for (int i = a; i < b + 1; i++)
        if (even(i) && is_prime(i))
            cnt++;
    cout << cnt;
    return 0;
}