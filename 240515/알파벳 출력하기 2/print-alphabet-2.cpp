#include <iostream>
using namespace std;

int main() {
    int n, c = 65;

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i > j)
                cout << "  ";
            else
                cout << (char) ((c++ - 'A') % 26 + 'A') << " ";
        }
        cout << '\n';
    }
    return 0;
}