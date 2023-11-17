#include <iostream>
using namespace std;

int main() {
    char arr[5][3];

    for(int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cin >> arr[i][j];
            arr[i][j] = arr[i][j] + 'A' - 'a';
            cout << arr[i][j] << " ";
        }
        cout << "\n";
    }
}