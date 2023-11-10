#include <iostream>
using namespace std;

int main() {
    int a;
    int b;
    int c;
    int temp;

    a = 5;
    b = 6;
    c = 7;

    temp = a;
    a = c;
    c = b;
    b = temp;
    cout << a << endl;
    cout << b << endl;
    cout << c;
    return 0;
}