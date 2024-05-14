#include <iostream>
using namespace std;

int main() {
    int a, b;
    bool exists;

    cin >> a >> b;
    for (int i = a; i < b + 1; i++){
        if (1920 % i == 0 && 2880 % i == 0){
            exists = true;
            break;
        }
    }
    if (exists)
        cout << 1;
    else
        cout << 0;
    return 0;
}