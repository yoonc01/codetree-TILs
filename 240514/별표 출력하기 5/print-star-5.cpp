#include <iostream>
using namespace std;

int main() {
    int n;

    cin >> n;

    for (int k = n; k > 0; k--)
    {
        for (int j = 0; j < k; j++)
        {
            for (int i = 0; i < k; i++)
                cout << "*";
            cout << " ";
        }
        cout << "\n";
    }
    return 0;
}