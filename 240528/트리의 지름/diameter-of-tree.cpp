#include <iostream>
#include <queue>
#include <tuple>
#include <algorithm>
#include <vector>

using namespace std;

int n, order;
vector<pair<int, int>> G[100000];
bool visited[100000];
int dist[100000];

void    dfs(int x)
{
    for (int i = 0; i < G[x].size(); i++)
    {
        int node, w;
        tie(node, w) = G[x][i];
        if (!visited[node])
        {
            order = order + w;
            dist[node] = order;
            visited[node] = true;
            dfs(node);
            order = order - w;
        }
    }
}

int main() {
    cin >> n;
    for (int i = 0; i < n - 1; i++)
    {
        int s, e, w;
        cin >> s >> e >> w;
        G[s - 1].push_back(make_pair(e - 1, w));
        G[e - 1].push_back(make_pair(s - 1, w));
    }

    visited[0] = true;
    order = 0;
    dfs(0);
    
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

    visited[max_idx] = true;
    order = 0;
    dfs(max_idx);

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