#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    double d;

    cin >> d;

    cout << fixed;
    cout.precision(1);
    cout << d * 30.48 << endl;
    return 0;
}