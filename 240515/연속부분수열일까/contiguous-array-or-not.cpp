#include <iostream>
using namespace std;

int main() {
    int n, m;
    int arr1[100] = {}, arr2[100] = {};
    bool check;

    cin >> n >> m;
    for (int i = 0; i < n; i++)
        cin >> arr1[i];
    
    for (int i = 0; i < m; i++)
        cin >> arr2[i];
    
    
    for (int i = 0; i < n - m + 1; i++)
    {
        check = true;
        for (int j = 0; j < m; j++)
        {
            if (arr1[i + j] != arr2[j])
            {
                check = false;
                break;
            }
        }
        if (check)
            break;
    }
    if (check)
        cout << "Yes";
    else
        cout << "No";
    return 0;
}