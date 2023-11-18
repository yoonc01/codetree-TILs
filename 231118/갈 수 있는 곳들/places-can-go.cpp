#include <iostream>
#include <queue>
using namespace std;

int arr[100][100] = {}, visited[100][100] = {};
int n, m;
queue<pair<int, int> >q;

int in_range(int x, int y)
{
	return (0 <= x && x < n && 0 <= y && y < n);
}

void bfs(int a, int b)
{
	q.push(make_pair(a, b));
	visited[a][b] = 1;
	int dx[4] = {1, 0, -1, 0};
	int dy[4] = {0, 1, 0, -1};

	while(!q.empty())
	{
		pair<int, int> curr_pos = q.front();
		int x = curr_pos.first, y = curr_pos.second;
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (in_range(nx, ny) && !visited[nx][ny] && !arr[nx][ny])
			{
				visited[nx][ny] = 1;
				q.push(make_pair(nx, ny));
			}
		}
	}
}

int main(){
	int cnt = 0;
	cin >> n >> m;

	for(int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
			cin >> arr[i][j];
	}
	for(int i = 0; i < m; i++)
	{
		int a, b;
		cin >> a >> b;
		a--;
		b--;
		bfs(a, b);
	}
	for(int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (visited[i][j])
				cnt++;
		}
	}
	cout << cnt;


}