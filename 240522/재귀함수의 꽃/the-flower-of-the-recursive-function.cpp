#include <iostream>
using namespace std;

void    seq(int n)
{
    if (n == 0)
        return ;
    cout << n << ' ';
    seq(n - 1);
    cout << n << ' ';
}

int main() {
    int n;

    cin >> n;
    seq(n);
    return 0;
}