#include <iostream>
using namespace std;

int main() {
    int n, m, arr[100][100] = {};
    int r, c;
    cin >> n >> m;

    for (int i = 1; i <= m; i++)
    {
        cin >> r >> c;
        arr[r - 1][c - 1] = i;
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            cout << arr[i][j] << ' ';
        cout << '\n';
    }
    return 0;
}