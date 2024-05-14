#include <iostream>
using namespace std;

int main() {
    int a;
    bool s = true;

    for (int i = 0; i < 5; i++)
    {
        cin >> a;
        if (a % 3 != 0)
        {
            s = false;
            break;
        }
    }
    if (s)
        cout << 1;
    else
        cout << 0;
    return 0;
}