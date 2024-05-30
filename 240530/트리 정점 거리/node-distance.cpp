#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int n, m;
vector <pair<int, int>> G[1000];
bool visited[1000];

int    bfs(int s, int e)
{
    for (int i = 0; i < n; i++)
        visited[i] = false;
    queue <pair<int, int>> q;
    visited[s] = true;
    q.push(make_pair(s, 0));
    while(!q.empty())
    {
        int x, w;
        tie(x, w) = q.front();
        q.pop();
        if (x == e)
            return w;
        for (int i = 0; i < G[x].size(); i++)
        {
            int to_idx, to_dist;
            tie(to_idx, to_dist) = G[x][i];
            if (!visited[to_idx])
            {
                visited[to_idx] = true;
                q.push(make_pair(to_idx, to_dist + w));
            }
        }
    }
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n - 1; i++)
    {
        int s, e, w;
        cin >> s >> e >> w;
        G[s - 1].push_back(make_pair(e - 1, w));
        G[e - 1].push_back(make_pair(s - 1, w));
    }

    for (int i = 0; i < m; i++)
    {
        int s, e;
        cin >> s >> e;
        cout << bfs(s - 1, e - 1) << '\n';
    }
    return 0;
}