class Solution {
public:
    string mostCommonWord(string paragraph, vector<string>& banned) {
        // Step 1: Put banned words in a set for fast O(1) lookups
        unordered_set<string> banned_set(banned.begin(), banned.end());
        
        // Step 2: Clean the paragraph by lowercasing and changing punctuation to spaces
        for (char &c : paragraph) {
            if (isalpha(c)) {
                c = tolower(c);
            } else {
                c = ' '; // Overwrites commas, periods, etc., to avoid combining words
            }
        }
        
        // Step 3: Stream through the clean words and track frequencies
        stringstream ss(paragraph);
        string word;
        unordered_map<string, int> word_counts;
        
        string result = "";
        int max_count = 0;
        
        while (ss >> word) {
            // Check if the word is allowed
            if (banned_set.find(word) == banned_set.end()) {
                word_counts[word]++;
                
                // Track the word with the highest frequency on the fly
                if (word_counts[word] > max_count) {
                    max_count = word_counts[word];
                    result = word;
                }
            }
        }
        
        return result;
    }
};