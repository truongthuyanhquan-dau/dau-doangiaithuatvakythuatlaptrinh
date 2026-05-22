

class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        int n = names.size();
        
        // Step 1: Create an index array: [0, 1, 2, ..., n-1]
        vector<int> indices(n);
        iota(indices.begin(), indices.end(), 0);
        
        // Step 2: Sort indices based on their corresponding heights in descending order
        sort(indices.begin(), indices.end(), [&](int a, int b) {
            return heights[a] > heights[b];
        });
        
        // Step 3: Populate the final result using the sorted order of indices
        vector<string> result;
        result.reserve(n);
        for (int index : indices) {
            result.push_back(names[index]);
        }
        
        return result;
    }
};