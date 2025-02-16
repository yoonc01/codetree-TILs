#include <iostream>
#include <string>
using namespace std;

void swap_chars(string &str, int a, int b) {
    swap(str[a - 1], str[b - 1]);
}

void change(string &str, char a, char b) {
    for (size_t i = 0; i < str.length(); i++) {
        if (str[i] == a) str[i] = b;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    string str;

    cin >> str >> t;

    while (t--) {
        int cmd;
        cin >> cmd;

        if (cmd == 1) {
            int a, b;
            cin >> a >> b;
            swap_chars(str, a, b);
        } else {
            char a, b;
            cin >> a >> b;
            change(str, a, b);
        }

        cout << str << "\n";
    }

    return 0;
}
