class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        // Step 1: Count how many times each number appears
        // Using size 102 to safely handle elements up to 100 without out-of-bounds errors
        vector<int> count(102, 0);
        for (int num : nums) {
            count[num]++;
        }
        
        // Step 2: Transform counts into prefix sums
        // After this loop, count[i] tells us how many elements are <= i
        for (int i = 1; i <= 100; i++) {
            count[i] += count[i - 1];
        }
        
        // Step 3: Map the values back to the original array positions
        vector<int> result;
        for (int num : nums) {
            if (num == 0) {
                result.push_back(0); // Nothing can be smaller than 0
            } else {
                // The total count of elements strictly smaller than 'num' 
                // is stored at 'num - 1'
                result.push_back(count[num - 1]);
            }
        }
        
        return result;
    }
};