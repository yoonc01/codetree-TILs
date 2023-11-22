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
        dp[i] = INT_MAX;
    
    for (int i = 1; i <= m; i++){
        for (int j = 0; j < n; j++){
            if (i - coin[j] >= 0 && dp[i - coin[j]] != INT_MAX) //아까는 파이썬이라 오버플로우 발생이 되지 않아서 문제가 없었던 듯 심지어 min으로 하고 있으니까 뒤의 조건을 추가시켜주는 게 맞다.
                dp[i] = min(dp[i - coin[j]] + 1, dp[i]);
        }
    }

    if (dp[m] != INT_MAX)
        cout << dp[m];
    else
        cout << -1;
    return 0;
}