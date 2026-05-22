class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_set<string> starting_cities;
        
        // Collect all origin cities (index 0 of each path)
        for (const auto& path : paths) {
            starting_cities.insert(path[0]);
        }
        
        // Find the destination city (index 1) that is never used as a starting city
        for (const auto& path : paths) {
            if (starting_cities.find(path[1]) == starting_cities.end()) {
                return path[1];
            }
        }
        
        return "";
    }
};
