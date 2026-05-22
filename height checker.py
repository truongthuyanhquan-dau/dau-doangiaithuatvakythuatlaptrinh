class Solution {
public:
    int heightChecker(vector<int>& heights) {
        // Create an expected array which represents the correct, sorted order
        vector<int> expected = heights;
        sort(expected.begin(), expected.end());
        
        int count = 0;
        
        // Compare index by index
        for (int i = 0; i < heights.size(); i++) {
            if (heights[i] != expected[i]) {
                count++;
            }
        }
        
        return count;
    }
};