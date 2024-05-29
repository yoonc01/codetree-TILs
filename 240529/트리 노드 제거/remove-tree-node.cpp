#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, del, start;
int parents[50];
vector <int> G[50];

int bfs(int s)
{
    if (s == del)
        return 0;
    int cnt = 0;
    queue <int> q;
    q.push(s);
    while(!q.empty())
    {
        int x = q.front();
        q.pop();
        bool is_leaf = true;
        for (int i = 0; i < G[x].size(); i++)
        {
            int child = G[x][i];
            if (child == del)
                continue;
            q.push(child);
            is_leaf = false;
        }
        if (is_leaf)
            cnt++;
    }
    return (cnt);
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> parents[i];
    cin >> del;

    for (int i = 0; i < n; i++)
    {
        int child = i, parent = parents[i];
        if (parent == -1)
        {
            start = child;
            continue;
        }
        G[parent].push_back(child);
    }
    cout << bfs(start);

    return 0;
}