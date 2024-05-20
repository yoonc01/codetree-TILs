#include <iostream>
using namespace std;

int foo(int n)
{
    int total = 0;
    for (int i = 1; i < n + 1; i++)
        total = total + i;
    return (total / 10);
}

int main() {
    int n;

    cin >> n;
    cout << foo(n);
    return 0;
}