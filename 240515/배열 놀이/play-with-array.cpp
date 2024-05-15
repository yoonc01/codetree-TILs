#include <iostream>
using namespace std;

int main() {
    int n, q;
    int arr[101] = {};

    cin >> n >> q;
    for(int i = 0; i < n; i++)
        cin >> arr[i];
    for(int i = 0; i < q; i++)
    {
        int cmd;
        cin >> cmd;
        if (cmd == 1)
        {
            int idx;
            cin >> idx;
            cout << arr[idx - 1];
        }
        if (cmd == 2)
        {
            int b;
            int idx = -1;
            cin >> b;
            for (int i = 0; i < n; i++)
                if (arr[i] == b)
                {
                    idx = i;
                    break;
                }
            if (idx == -1)
                cout << 0;
            else
                cout << idx + 1;
        }
        if (cmd == 3)
        {
            int s, e;
            cin >> s >> e;
            for (int i = s - 1; i < e; i++)
                cout << arr[i] << ' ';
        }
        cout << '\n';
    }
    return 0;
}