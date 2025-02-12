#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int total = 0;
    string str;
    for (int i = 0; i < 10; i++)
    {
        cin >> str;
        total = total + str.length();
    }
    cout << total;
    return 0;
}