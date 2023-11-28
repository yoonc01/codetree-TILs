#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector <int> v;
int n, a;
string cmd;

int main() {
    cin >> n;
    while(n--){
        cin >> cmd;
        if (cmd.compare("push_back") == 0){
            cin >> a;
            v.push_back(a);
        }
        else if (cmd.compare("pop_back") == 0){
            v.pop_back();
        }
        else if (cmd.compare("size") == 0){
            cout << v.size() << '\n';
        }
        else if (cmd.compare("get") == 0){
            cin >> a;
            cout << v[a - 1] << '\n';
        }
    }
    return 0;
}