#include <iostream>
#include <queue>

using namespace std;

int n, k, ans;
int arr[100][100];
bool visited[100][100];
queue <pair<int, int>> q;

bool in_range(int x, int y)
{
    return (0 <= x && x < n && 0 <= y && y < n);
}

int bfs(int a, int b)
{
    int cnt = 1;
    visited[a][b] = true;
    q.push(make_pair(a, b));
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};
    while(!q.empty())
    {
        pair<int, int> pos = q.front();
        int x = pos.first, y = pos.second;
        q.pop();
        for (int dir = 0; dir < 4; dir++)
        {
            int nx = x + dx[dir], ny = y + dy[dir];
            if (in_range(nx, ny) && !arr[nx][ny] && !visited[nx][ny])
            {
                cnt++;
                visited[nx][ny] = true;
                q.push(make_pair(nx, ny));
            }
        }
    }
    return (cnt);
}

int main() {
    cin >> n >> k;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> arr[i][j];
    for (int i = 0; i < k; i++)
    {
        int a, b;
        cin >> a >> b;
        if (!visited[a - 1][b - 1])
            ans = ans + bfs(a - 1, b - 1);
    }
    cout << ans;
    return 0;
}