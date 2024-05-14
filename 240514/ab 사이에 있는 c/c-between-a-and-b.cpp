#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    bool satisfied = false;
    cin >> a >> b >> c;

    for (int i = a; i < b + 1; i++)
    {
        if (i % c == 0)
        {
            satisfied = true;
            break;
        }
    }
    if (satisfied)
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }
    return 0;
}