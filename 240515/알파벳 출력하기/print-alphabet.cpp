#include <iostream>
using namespace std;

int main() {
    int n;
    char c = 65;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i + 1; j++)
        {
            cout << (char) ((c - 65) % 26 + 65);
            c++;
        }
        cout << '\n';
    }
    return 0;
}