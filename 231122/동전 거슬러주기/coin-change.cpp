#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int n, m;
int coin[100];
int dp[100001];

int main() {
    cin >> n >> m;
    for(int i = 0; i < n; i++)
        cin >> coin[i];
    
    dp[0] = 0;
    for(int i = 1; i <= m; i++)
        dp[i] = 100001;
    
    for (int i = 1; i <= m; i++){
        for (int j = 0; j < n; j++){
            if (i - coin[j] >= 0)
                dp[i] = min(dp[i - coin[j]] + 1, dp[i]);
        }
    }

    if (dp[m] != INT_MAX)
        cout << dp[m];
    else
        cout << -1;
    return 0;
}