#include <iostream>
using namespace std;

int main() {
    int first = -2147483648, second = -2147483648;

    int n;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;

        if (num > first)
        {
            second = first;
            first = num;
        }
        else if (num > second)
        {
            second = num;
        }
    }
    cout << first << ' ' << second;
    return 0;
}