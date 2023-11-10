#include <iostream>
using namespace std;

int main() {
    int a;
    int b;
    int temp;

    a = 2;
    b = 5;
    temp = a;
    a = b;
    b = temp;
    cout << a << endl << b;
    return 0;
}