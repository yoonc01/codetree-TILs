#include <iostream>
#include <climits>
using namespace std;

int main() {
    int n, max_val;

    max_val = INT_MIN;
    for(int i = 0; i < 10; i++){
        cin >> n;
        if (n > max_val)
            max_val = n;
    }
    cout << max_val;
    return 0;
}