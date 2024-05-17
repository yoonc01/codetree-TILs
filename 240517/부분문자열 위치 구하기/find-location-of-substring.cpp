#include <iostream>
#include <string>
using namespace std;

int main() {
    string str, to_find;
    int idx = -1;
    cin >> str >> to_find;

    if (str.find(to_find) != string::npos)
        idx = str.find(to_find);
    cout << idx;

    return 0;
}