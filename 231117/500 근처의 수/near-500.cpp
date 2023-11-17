#include <iostream>
#include <climits>
using namespace std;

int main() {
    int n, max_val, min_val;
    
    max_val = INT_MIN;
    min_val = INT_MAX;
    for(int i = 0; i < 10; i++)
    {
        cin >> n;
        if (n > 500 && n < min_val)
            min_val = n;
        else if (n < 500 && n > max_val)
            max_val = n;
    }
    cout << max_val << " " << min_val;
    return 0;
}