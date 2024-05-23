#include <iostream>

using namespace std;

int main() {
    int h, m, to_h, to_m;
    int total_time = 0;

    cin >> h >> m >> to_h >> to_m;

    while(1){
        if (h == to_h && m == to_m)
            break;
        total_time++;
        m++;
        if (m == 60){
            m = 0;
            h++;
        }
    }
    cout << total_time;
    return 0;
}