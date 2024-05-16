#include <iostream>
using namespace std;

int main() {
    int arr[4][4];

    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
            cin >> arr[i][j];
    }
    int sum_val = 0;
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (j <= i)
                sum_val = sum_val + arr[i][j];
        }
    }
    cout << sum_val;
    return 0;
}