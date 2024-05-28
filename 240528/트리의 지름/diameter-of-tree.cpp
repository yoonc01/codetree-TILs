#include <iostream>
#include <queue>
#include <tuple>
#include <algorithm>
#include <vector>

using namespace std;

int n;
vector<pair<int, int>> G[100000];
bool visited[100000];
int dist[100000];

void    bfs(int s)
{
    queue <pair<int, int>> q;
    visited[s] = true;
    dist[s] = 0;
    q.push(make_pair(s, 0));
    while(!q.empty())
    {
        int x, w;
        tie(x, w) = q.front();
        q.pop();
        for (int i = 0; i < G[x].size(); i++)
        {
            int to_idx, to_dist;
            tie(to_idx, to_dist) = G[x][i];
            if (!visited[to_idx])
            {
                visited[to_idx] = true;
                dist[to_idx] = w + to_dist;
                q.push(make_pair(to_idx, dist[to_idx]));
            }
        }
    }
}

int main() {
    cin >> n;
    for(int i = 0; i < n - 1; i++)
    {
        int s, e, w;
        cin >> s >> e >> w;
        G[s - 1].push_back(make_pair(e - 1, w));
        G[e - 1].push_back(make_pair(s - 1, w));
    }

    bfs(0);    
    int max_val = -1, max_idx = -1;
    for (int i = 0; i < n; i++)
    {
        if (dist[i] > max_val)
        {
            max_val = dist[i];
            max_idx = i;
        }
    }

    for (int i = 0; i < n; i++)
    {
        dist[i] = 0;
        visited[i] = false;
    }

    bfs(max_idx);
    max_val = -1;
    max_idx = -1;
    for (int i = 0; i < n; i++)
    {
        if (dist[i] > max_val)
        {
            max_val = dist[i];
            max_idx = i;
        }
    }

    cout << max_val;
    return 0;
}