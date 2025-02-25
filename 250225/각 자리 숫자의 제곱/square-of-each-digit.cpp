#include <iostream>

using namespace std;

int get_square_total(int n) {
    if (n < 10)
        return n * n;
    int digit = n % 10;
    return get_square_total(n / 10) + digit * digit;
}

int main() {
    int n;
    cin >> n;

    cout << get_square_total(n);
    return 0;
}