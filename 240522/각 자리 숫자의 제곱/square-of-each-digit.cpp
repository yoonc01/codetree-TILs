#include <iostream>
using namespace std;

int seq(int n)
{
    if (n < 10)
        return (n * n);
    return (seq(n - 1) + n * n);
}

int main() {
    int n;

    cin >> n;
    cout << seq(n);
    return 0;
}