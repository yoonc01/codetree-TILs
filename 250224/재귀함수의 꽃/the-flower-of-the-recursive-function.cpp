#include <iostream>

using namespace std;

void printCnt(int n) {
    if (n == 0)
        return;
    cout << n << " ";
    printCnt(n - 1);
    cout << n << " ";
}

int main() {
    int n;
    cin >> n;

    printCnt(n);
    return 0;
}