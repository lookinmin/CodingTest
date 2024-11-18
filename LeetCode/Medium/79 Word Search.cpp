#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int dx[4] = {0, 0, -1, 1};
    int dy[4] = {-1, 1, 0, 0};
    int n, m;
    vector<vector<int>> visited;
    vector<vector<char>> board;
    string target;

    // dfs 함수에서 필요한 변수들은 모두 클래스 멤버 변수로 접근
    bool dfs(int x, int y, int idx) {
        if (board[x][y] != target[idx]) return false;
        if (idx == target.size() - 1) return true;

        visited[x][y] = 1; // 현재 위치 방문 표시

        // 상하좌우 탐색
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && visited[nx][ny] == 0) {
                if (dfs(nx, ny, idx + 1)) {
                    return true;
                }
            }
        }

        visited[x][y] = 0; // 백트래킹
        return false;
    }

    bool exist(vector<vector<char>>& inputBoard, string word) {
        board = inputBoard; // 입력을 멤버 변수로 할당
        target = word;
        n = board.size();
        m = board[0].size();
        visited = vector<vector<int>>(n, vector<int>(m, 0));

        // 모든 셀을 시작점으로 시도
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == word[0]) {
                    if (dfs(i, j, 0)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
};
