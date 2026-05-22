class Solution {
public:
    vector<int> sumZero(int n) {
        vector<int> result;
        
        // If n is odd, adding a single 0 keeps the total sum at 0
        if (n % 2 != 0) {
            result.push_back(0);
        }
        
        // Keep adding symmetric pairs (1, -1), (2, -2)... until the vector reaches size n
        for (int i = 1; result.size() < n; i++) {
            result.push_back(i);
            result.push_back(-i);
        }
        
        return result;
    }
};