#include <iostream>
using namespace std;

int main() {
    int n;
    int cnt;

    cin >> n;
    cnt = 1;

    for (int i = 0; i < 2 * n; i++)
    {
        for (int j = 0; j < cnt; j++)
        {
            cout << "* ";
        }
        cout << "\n";
        if (i < n - 1)
            cnt++;
        else
            cnt--;
    }

    return 0;
}