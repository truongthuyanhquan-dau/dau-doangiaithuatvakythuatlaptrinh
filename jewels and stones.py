class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        // Lookups in an unordered_set take O(1) time on average
        unordered_set<char> jewel_set(jewels.begin(), jewels.end());
        int count = 0;
        
        // Loop through each stone you have
        for (char stone : stones) {
            // If the stone exists in our jewel set, count it
            if (jewel_set.count(stone)) {
                count++;
            }
        }
        
        return count;
    }
};