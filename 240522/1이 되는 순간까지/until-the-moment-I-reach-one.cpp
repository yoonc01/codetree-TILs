#include <iostream>
using namespace std;

int foo(int n)
{
    if (n == 1)
        return (0);
    if (n % 2 == 0)
        return (foo(n / 2) + 1);
    else
        return (foo(n / 3) + 1);
}

int main() {
    int n;

    cin >> n;
    cout << foo(n);
    return 0;
}