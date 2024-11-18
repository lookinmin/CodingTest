#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int dx[4] = {0, 0, -1, 1};
    int dy[4] = {-1, 1, 0, 0};
    int n, m;

    bool dfs(int x, int y, int idx, string& target, vector<vector<char>>& board, vector<vector<int>>& visited) {
        if (board[x][y] != target[idx]) return false;
        if (idx == target.size() - 1) return true;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m && visited[nx][ny] == 0) {
                visited[x][y] = 1; 
                if (dfs(nx, ny, idx + 1, target, board, visited)) {
                    return true; 
                }
                visited[x][y] = 0;
            }
        }
        return false;
    }

    bool exist(vector<vector<char>>& board, string word) {
        n = board.size();
        m = board[0].size();
        vector<vector<int>> visited(n, vector<int>(m, 0));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == word[0]) {
                    if (dfs(i, j, 0, word, board, visited)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }
};
