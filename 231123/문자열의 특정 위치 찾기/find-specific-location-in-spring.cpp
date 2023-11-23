#include <iostream>
#include <string>
using namespace std;

int main() {
    string str, to_find;
    cin >> str >> to_find;
    if (str.find(to_find) != string::npos)
        cout << str.find(to_find);
    else
        cout << "No";
    return 0;
}