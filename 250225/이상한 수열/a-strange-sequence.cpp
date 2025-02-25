#include <iostream>

using namespace std;

int n;

int seq(int n) {
    if (n == 1)
        return 1;
    if (n == 2)
        return 2;
    return seq(n / 3) + seq(n - 1);
}

int main() {
    cin >> n;
    
    cout << seq(n);
    return 0;
}