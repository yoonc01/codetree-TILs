#include <iostream>
#include <algorithm>
using namespace std;

int arr[1000];
int dp[1000];
int n, max_val = 0;

int main() {
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> arr[i];
        dp[i] = -1;
    }
    dp[0] = 0;
    for (int i = 0; i < n; i++){
        for(int j = 0; j < i; j++){
            if (arr[j] + j >= i && dp[j] != -1)
                dp[i] = max(dp[i], dp[j] + 1);
        }
        max_val = max(max_val, dp[i]);
    }
    cout << max_val;
    return 0;
}