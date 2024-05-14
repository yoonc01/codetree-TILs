#include <iostream>
using namespace std;

int main() {
    int n;
    bool is_prime = true;

    cin >> n;

    for (int i = 2; i < n; i++)
    {
        if (n % i == 0)
        {
            is_prime = false;
            break;
        }
    }
    if (is_prime)
        cout << "P";
    else
        cout << "C";
    return 0;
}