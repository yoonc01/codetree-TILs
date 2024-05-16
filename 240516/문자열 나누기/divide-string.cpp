#include <iostream>
#include <string>
using namespace std;

int main() {
    string arr[10];
    string result = "";
    int n;

    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    for (int i = 0; i < n; i++)
        result = result + arr[i];
    
    for (int i = 0; i < result.length(); i++)
    {
        cout << result[i];
        if ((i + 1) % 5 == 0)
            cout << '\n';
    }
    return 0;
}