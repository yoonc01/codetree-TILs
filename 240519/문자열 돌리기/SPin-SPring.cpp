#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    cin >> str;

    int len = str.length();
    cout << str << '\n';
    for (int i = 0; i < len; i++)
    {
        str = str.substr(len - 1, 1) + str.substr(0, len - 1);
        cout << str << '\n';
    }
    return 0;
}