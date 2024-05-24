#include <iostream>
#include <queue>
#include <vector>
#include <tuple>

using namespace std;

int n, m;
int dist[1000], path[1000];
int G[1000][1000];
priority_queue <pair<int, int>> pq;

int main() {
    cin >> n >> m;
    while(m--)
    {
        int s, e, w;
        cin >> s >> e >> w;
        G[s - 1][e - 1] = w;
        G[e - 1][s - 1] = w;
    }
    int s, e;
    cin >> s >> e;

    for (int i = 0; i < n; i++)
        dist[i] = 2147483647;
    dist[e - 1] = 0;
    pq.push(make_pair(0, e - 1));
    while (!pq.empty())
    {
        int min_dist, min_idx;
        tie(min_dist, min_idx) = pq.top();
        pq.pop();
        min_dist = -min_dist;

        if (dist[min_idx] != min_dist)
            continue;
        
        for (int i = 0; i < n; i++)
        {
            if (G[min_idx][i] == 0)
                continue;
            
            int new_dist = dist[min_idx] + G[min_idx][i];
            if (new_dist < dist[i])
            {
                dist[i] = new_dist;
                pq.push(make_pair(-new_dist, i));
                path[i] = min_idx;
            }
        }
    }
    cout << dist[s - 1] << '\n';
    int x = s - 1;
    cout << x + 1 << ' ';
    while (x != e - 1)
    {
        for (int i = 0; i < n; i++)
        {
            if (G[i][x] == 0)
                continue;
            if (dist[x] == G[i][x] + dist[i]){
                x = i;
                break;
            }
        }
        cout << x + 1 << ' ';
    }
    return 0;
}