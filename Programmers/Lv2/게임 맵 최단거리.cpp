#include <vector>
#include <queue>
using namespace std;

int bfs(vector<vector<int>>& visited, vector<vector<int>>& graph, int n, int m) {
    vector<int> dx = {-1, 1, 0, 0};
    vector<int> dy = {0, 0, -1, 1};
    
    queue<pair<pair<int, int>, int>> q;
    q.push({{0, 0}, 1}); // {좌표, 이동 횟수}
    visited[0][0] = 1;
    
    while (!q.empty()) {
        auto [coord, cnt] = q.front();
        int x = coord.first;
        int y = coord.second;
        q.pop();

        // 도착 지점에 도달한 경우
        if (x == n - 1 && y == m - 1) {
            return cnt;
        }
        
        // 4방향 탐색
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            // 범위 내에 있고, 이동 가능한 위치이며, 방문하지 않은 경우
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && graph[nx][ny] == 1 && visited[nx][ny] == 0) {
                visited[nx][ny] = 1; // 방문 체크를 큐에 넣기 전에 수행
                q.push({{nx, ny}, cnt + 1});
            }
        }
    }
    
    return -1; // 도착 지점에 도달할 수 없는 경우
}

int solution(vector<vector<int>> maps) {
    int n = maps.size();
    int m = maps[0].size();
    
    vector<vector<int>> visited(n, vector<int>(m, 0));
    return bfs(visited, maps, n, m);
}
