#include <string>
#include <iostream>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string str;
    while (true) {
        cin >> str;
        if (str == "END")
            break;
        size_t length = str.size();
        for (size_t i = 0; i < length; i++)
            cout << str[length - i - 1];
        cout << "\n";
    }
    return 0;
}