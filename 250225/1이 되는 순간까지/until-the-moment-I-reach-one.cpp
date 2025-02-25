#include <iostream>

using namespace std;

int until_one(int n) {
    if (n == 1)
        return 0;
    if (n % 2 == 0)
        return until_one(n / 2) + 1;
    else
        return until_one(n / 3) + 1;
}

int main() {
    int n;
    cin >> n;

    cout << until_one(n);
    return 0;
}