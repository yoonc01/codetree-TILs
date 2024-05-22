#include <iostream>
using namespace std;

int foo(int n)
{
    if (n == 1)
        return (1);
    else if (n == 2)
        return (2);
    else
        return (foo(n - 2) + n);
}

int main() {
    int n;

    cin >> n;
    cout << foo(n);
    return 0;
}