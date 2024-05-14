#include <iostream>
using namespace std;

int main() {
    int n;
    bool c = false;
    cin >> n;

    for (int i = 2; i < n; i++)
    {
        if (n % i == 0)
        {
            c = true;
            break;
        }
    }
    if (c)
        cout << "C";
    else
        cout << "N";
    return 0;
}