#include <iostream>
#include <string>
using namespace std;

int main() {
    char c;
    double a, b;

    cin >> c >> a >> b;
    cout << fixed;
    cout.precision(2);
    cout << c << endl;
    cout << a << endl;
    cout << b;
    return 0;
}