#include <iostream>
using namespace std;

int main() {
    int n;
    int cnt = 0;

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << cnt % 9 + 1;
            cnt++;
        }
        cout << "\n";
    }
    return 0;
}