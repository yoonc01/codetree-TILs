#include <iostream>

using namespace std;

int n;

int get_total(int n)
{
    if (n == 1)
        return 1;
    return get_total(n - 1) + n;
}

int main() {
    cin >> n;

    cout << get_total(n);
    return 0;
}