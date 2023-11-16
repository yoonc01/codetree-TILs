#include <iostream>
using namespace std;

int main() {
    int n;
    int count_arr[10] = {};

    cin >> n;
    for(int i = 0; i < n; i++){
        int num;
        cin >> num;
        count_arr[num] = count_arr[num] + 1;
    }
    for(int i = 1; i < 10; i++){
        cout << count_arr[i] << "\n";
    }
    return 0;
}