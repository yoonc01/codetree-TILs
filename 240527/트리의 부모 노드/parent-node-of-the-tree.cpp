#include <iostream>
#include <vector>

using namespace std;

int n;
vector <int> G[100000];
bool visited[100000];
int parent[100000];

void	travel(int x)
{
	for (int i = 0; i < G[x].size(); i++)
	{
		int	node = G[x][i];
		if (!visited[node])
		{
			parent[node] = x;
			visited[node] = true;
			travel(node);
		}
	}
}

int main()
{
	cin >> n;
	for (int i = 0; i < n - 1; i++)
	{
		int s, e;
		cin >> s >> e;
		G[s - 1].push_back(e - 1);
		G[e - 1].push_back(s - 1);
	}
	visited[0] = true;
	travel(0);

	for (int i = 1; i < n; i++)
		cout << parent[i] + 1 << '\n';
}