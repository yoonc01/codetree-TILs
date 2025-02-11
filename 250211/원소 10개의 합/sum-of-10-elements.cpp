#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int val, sum = 0;
    for (int i = 0; i < 10; i++) {
        cin >> val;
        sum = sum + val;
    }
    cout << sum;
    return 0;
}