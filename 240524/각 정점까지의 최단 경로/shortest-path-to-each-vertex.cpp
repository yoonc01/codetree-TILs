#include <iostream>
#include <queue>
#include <tuple>

using namespace std;

int n, m, k;
vector <pair<int, int>> G[20000];
priority_queue<pair<int, int>> pq;

int dist[20000];

int main() {
    cin >> n >> m >> k;
    for (int i = 0; i < m; i++)
    {
        int s, e, w;
        cin >> s >> e >> w;
        G[s - 1].push_back(make_pair(e - 1, w));
        G[e - 1].push_back(make_pair(s - 1, w));
    }
    for (int i = 0; i < n; i++)
        dist[i] = 2147483647;
    
    dist[k - 1] = 0;
    pq.push(make_pair(0, k - 1));
    while (!pq.empty())
    {
        int min_dist, min_index;
        tie(min_dist, min_index) = pq.top();
        pq.pop();
        min_dist = -min_dist;

        if (min_dist != dist[min_index])
            continue;
        
        for (int i = 0; i < G[min_index].size(); i++)
        {
            int to_idx, to_dist;
            tie(to_idx, to_dist) = G[min_index][i];

            int new_dist = dist[min_index] + to_dist;
            if (new_dist < dist[to_idx])
            {
                dist[to_idx] = new_dist;
                pq.push(make_pair(-new_dist, to_idx));
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        if (dist[i] != 2147483647)
            cout << dist[i];
        else
            cout << -1;
        cout << '\n';
    }


    return 0;
}