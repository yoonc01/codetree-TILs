#include <iostream>
#include <climits>
using namespace std;

int main() {
    int n, num, first, second;

    cin >> n;
    first = INT_MIN;
    second = INT_MIN;
    for(int i = 0; i < n; i++)
    {
        cin >> num;
        if (num > first)
        {
            second = first;
            first = num;
        }
        else if (num > second)
            second = num;
    }
    cout << first << " " << second;
    return 0;
}