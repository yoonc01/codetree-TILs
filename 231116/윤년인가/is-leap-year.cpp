#include <iostream>
using namespace std;

int main() {
    int y;
    cin >> y;

    if (y % 400 == 0 || (y % 4 == 0 && y % 100 != 0))
        cout << "true";
    else
        cout << "false";
    return 0;
}