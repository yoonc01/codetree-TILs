#include <iostream>
#include <queue>
using namespace std;

int n, m;
bool visited[100][100] = {};
queue <pair<int, int> > q;
int arr[100][100] = {};

bool in_range(int x, int y)
{
	return (0 <= x && x < n && 0 <= y && y < m);
}

void bfs(){
	q.push(make_pair(0, 0));
	visited[0][0] = true;
	while(!q.empty())
	{
		pair<int, int>curr_pos = q.front();
		int x = curr_pos.first;
		int y = curr_pos.second;
		q.pop();

		int dx[4] = {1, 0, -1, 0};
		int dy[4] = {0, 1, 0, -1};

		for(int dir = 0; dir < 4; dir++){
			int nx = x + dx[dir];
			int ny = y + dy[dir];

			if (in_range(nx, ny) && !visited[nx][ny] && arr[nx][ny])
			{
				q.push(make_pair(nx, ny));
				visited[nx][ny] = true;
			}
		}
	}
}

int main(){

	cin >> n >> m;
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++)
			cin >> arr[i][j];
	}
	bfs();

	cout << visited[n - 1][m - 1];
}