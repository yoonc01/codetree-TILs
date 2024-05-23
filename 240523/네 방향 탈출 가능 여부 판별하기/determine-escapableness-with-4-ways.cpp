#include <iostream>
#include <queue>

using namespace std;

int     arr[100][100];
bool    visited[100][100];
int n, m;
queue<pair<int, int>> q;

bool    in_range(int x, int y)
{
    return (0 <= x && x < n && 0 <= y && y < m);
}

void    bfs(int a, int b){
    q.push(make_pair(a, b));
    visited[a][b] = true;
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};
    while(!q.empty())
    {
        pair<int, int> pos = q.front();
        q.pop();
        int x = pos.first, y = pos.second;
        for (int dir = 0; dir < 4; dir++)
        {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (in_range(nx, ny) && arr[nx][ny] && !visited[nx][ny])
            {
                visited[nx][ny] = true;
                q.push(make_pair(nx, ny));
            }
        }
    }
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> arr[i][j];
    bfs(0, 0);
    cout << visited[n - 1][m - 1];    

    return 0;
}