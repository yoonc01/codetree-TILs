#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    string str;

    for (int i = 0; i < 10; i++)
    {
        cin >> str;
        cout << str << '\n';
    }
    return 0;
}