#include <iostream>
using namespace std;

int main() {
    char arr[10];

    for (int i = 0; i < 10; i++){
        cin >> arr[i];
    }
    for (int i = 9; i >= 0; i--){
        cin >> arr[i];
    }
    return 0;
}