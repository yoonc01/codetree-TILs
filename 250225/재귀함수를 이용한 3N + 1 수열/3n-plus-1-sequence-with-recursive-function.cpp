#include <iostream>

using namespace std;

int n;

int count(int n) {
    if (n == 1)
        return 0;
    if (n % 2 == 0)
        return count(n / 2) + 1;
    return count(3 * n + 1) + 1;
}

int main() {
    cin >> n;

    cout << count(n);
    return 0;
}