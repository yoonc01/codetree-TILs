#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    bool not_exists = true;

    cin >> a >> b >> c;
    for (int i = a; i < b + 1; i++)
    {
        if (i % c == 0)
        {
            not_exists = false;
            break;
        }
    }
    if (not_exists)
    {
        cout << "YES";
    }
    else
        cout << "NO";
    return 0;
}