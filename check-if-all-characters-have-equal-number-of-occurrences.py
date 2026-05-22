class Solution {
public:
    bool areOccurrencesEqual(string s) {
        // Step 1: Count the occurrences of each lowercase English letter
        vector<int> freq(26, 0);
        for (char c : s) {
            freq[c - 'a']++;
        }
        
        int target_freq = -1;
        
        // Step 2: Ensure all characters that appeared have identical counts
        for (int i = 0; i < 26; i++) {
            if (freq[i] > 0) {
                if (target_freq == -1) {
                    target_freq = freq[i]; // Establish the baseline frequency
                } else if (freq[i] != target_freq) {
                    return false; // Found an uneven distribution
                }
            }
        }
        
        return true;
    }
};