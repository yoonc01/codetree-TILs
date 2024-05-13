#include <iostream>
using namespace std;

int main() {
    double a;

    cout << fixed;
    cout.precision(1);
    cin >> a;
    cout << a * 30.48;
    return 0;
}