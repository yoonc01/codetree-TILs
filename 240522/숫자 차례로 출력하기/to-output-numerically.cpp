#include <iostream>
using namespace std;

void    des(int n)
{
    if (n == 0)
        return ;
    cout << n << ' ';
    des(n - 1);
}

void asc(int n)
{
    if (n == 0)
        return ;
    asc(n - 1);
    cout << n << ' ';
}

int main() {
    int n;

    cin >> n;
    asc(n);
    cout << '\n';
    des(n);
    return 0;
}