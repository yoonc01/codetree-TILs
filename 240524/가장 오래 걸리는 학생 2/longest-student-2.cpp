#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>

using namespace std;

int n, m, dist[100000];
vector<pair<int, int>> G[100000];
priority_queue<pair<int, int>> pq;

int main() {
    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        int s, e, w;
        cin >> s >> e >> w;
        G[e - 1].push_back(make_pair(s - 1, w));
    }

    for (int i = 0; i < n; i++)
        dist[i] = 2147483647;
    
    dist[n - 1] = 0;
    pq.push(make_pair(0, n - 1));
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
            }
        }
    }
    int ans = 0;
    for (int i = 0; i < n; i++)
        ans = max(ans, dist[i]);
    
    cout << ans;
    return 0;
}