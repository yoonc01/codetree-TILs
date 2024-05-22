#include <iostream>
using namespace std;

int seq(int n)
{
    if (n < 10)
        return (n * n);
    return (seq(n / 10) + (n % 10) * (n % 10));
}

int main() {
    int n;

    cin >> n;
    cout << seq(n);
    return 0;
}