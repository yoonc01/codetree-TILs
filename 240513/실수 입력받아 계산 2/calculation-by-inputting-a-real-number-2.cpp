#include <iostream>
using namespace std;

int main() {
    double a;

    cout << fixed;
    cout.precision(2);
    cin >> a;
    cout << a + 1.5;
    return 0;
}