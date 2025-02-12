#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string str;
    cin >> str;

    string result;
    int idx = 0;

    while (idx < str.length()) {
        char current = str[idx];
        int count = 0;

        while (str[idx] == current) {
            idx++;
            count++;
        }

        result += current;
        result += to_string(count);
    }

    cout << result.length() << "\n" << result << "\n";
    return 0;
}
