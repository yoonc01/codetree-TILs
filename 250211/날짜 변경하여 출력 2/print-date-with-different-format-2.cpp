#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int y, m, d;
    char dummy;

    cin >> m >> dummy >> d >> dummy >> y;

    cout << y << "." << m << "." << d << endl;
    return 0;
}