class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        std::unordered_set<int> uniqueTypes(candyType.begin(), candyType.end());
        
        
        int maxAllowed = candyType.size() / 2;
        
        
        return std::min((int)uniqueTypes.size(), maxAllowed);
        
    }
};