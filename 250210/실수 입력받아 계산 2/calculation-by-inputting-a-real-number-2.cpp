#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    double d;

    cin >> d;

    cout << fixed;
    cout.precision(2);
    cout << d + 1.5 << endl;
    return 0;
}