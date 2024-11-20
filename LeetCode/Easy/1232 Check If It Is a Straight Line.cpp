class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int x1 = coordinates[0][0];
        int x2 = coordinates[1][0];
        int y1 = coordinates[0][1];
        int y2 = coordinates[1][1];

        int diff_x = x2 - x1;
        int diff_y = y2 - y1;
        
        for(int i = 2; i < coordinates.size(); i++){
            int x3 = coordinates[i][0];
            int y3 = coordinates[i][1];

            if(diff_y*(x3 - x2) != diff_x*(y3 - y2)) return false;
        }

        return true;
    }
};