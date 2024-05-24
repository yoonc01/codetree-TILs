#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int n, m;
vector <pair<int, int>> G[1000];
priority_queue <pair<int, int>> pq;
int dist[1000];
int path[1000];

int main() {
    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        int s, e, w;
        cin >> s >> e >> w;
        G[s - 1].push_back(make_pair(e - 1, w));
        G[e - 1].push_back(make_pair(s - 1, w));
    }
    int s, e;
    cin >> s >> e;

    for (int i = 0; i < n; i++)
        dist[i] = 2147483647;
    dist[s - 1] = 0;
    pq.push(make_pair(0, s - 1));
    while (!pq.empty())
    {
        int min_dist, min_idx;
        tie(min_dist, min_idx) = pq.top();
        pq.pop();
        min_dist = -min_dist;
        if (dist[min_idx] != min_dist)
            continue;
        for (int i = 0; i < G[min_idx].size(); i++)
        {
            int to_idx, to_dist;
            tie(to_idx, to_dist) = G[min_idx][i];
            
            int new_dist = dist[min_idx] + to_dist;
            if (new_dist < dist[to_idx])
            {
                dist[to_idx] = new_dist;
                pq.push(make_pair(-new_dist, to_idx));
                path[to_idx] = min_idx;
            }
        }
    }
    cout << dist[e - 1] << '\n';
    vector<int> paths;
    int x = e - 1;
    paths.push_back(x);
    while(x != s - 1)
    {
        x = path[x];
        paths.push_back(x);
    }
    for (int i = (int)paths.size() - 1; i > -1; i--)
        cout << paths[i] + 1 << ' ';
    return 0;
}