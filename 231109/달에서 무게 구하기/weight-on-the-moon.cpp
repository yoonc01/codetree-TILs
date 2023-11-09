#include <iostream>
using namespace std;

int main() {
    int w = 13;
    double g = 0.165;

    cout << fixed;
    cout.precision(6);

    cout << w << " * " << g << " = " << w * g;
    return 0;
}