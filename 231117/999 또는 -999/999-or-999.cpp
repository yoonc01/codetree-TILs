#include <iostream>
#include <climits>
using namespace std;

int main() {
    int n, min_val, max_val;

    min_val = INT_MAX;
    max_val = INT_MIN;
    while(1)
    {
        cin >> n;
        if (n == -999 || n == 999)
            break;
        else if (n > max_val)
            max_val = n;
        else if (n < min_val)
            min_val = n;
    }
    cout << max_val << " " << min_val;
    return 0;
}