#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;

    cin >> str;
    str = str.substr(1, str.length() - 1) + str[0];
    cout << str;
    return 0;
}