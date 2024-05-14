#include <iostream>
using namespace std;

int main() {
    int n;

    cin >> n;
    for (int i = 0; i < n; i++)
        cout << "* ";
    cout << "\n";
    for(int i = 1; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if (j < i)
                cout << "* ";
            else if (j >= i)
                cout << "  ";
        }
        cout <<"*\n";
    }
    return 0;
}