#include <iostream>
#include <string>

using namespace std;

string input_str;
string target_str;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> input_str;
    cin >> target_str;

    if (input_str.find(target_str) != string::npos) {
        cout << input_str.find(target_str);
    } else {
        cout << -1;
    }

    return 0;
}
