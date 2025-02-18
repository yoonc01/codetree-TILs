#include <iostream>

using namespace std;

void PrintRect(int n) {
    int cnt = 1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << cnt << " ";
            cnt = cnt % 9 + 1;
        }
        cout << "\n";
    }
}

int main() {
    int n;

    cin >> n;
    PrintRect(n);
    return 0;
}