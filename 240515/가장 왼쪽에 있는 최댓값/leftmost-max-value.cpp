#include <iostream>
using namespace std;

int main() {
    int max_val = -1, n;
    int idx[1000] = {}, j = 0;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int num;
        
        cin >> num;
        if (num > max_val)
        {
            max_val = num;
            idx[j++] = i + 1;
        }
    }
    for (int i = j - 1; i > -1; i--)
        cout << idx[i] << ' ';
    return 0;
}