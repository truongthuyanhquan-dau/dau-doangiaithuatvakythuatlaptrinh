using namespace std;

class Solution {
public:
    string toGoatLatin(string sentence) {
        // Helper lambda to quickly check if a character is a vowel
        auto isVowel = [](char c) {
            c = tolower(c);
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        };
        
        stringstream ss(sentence);
        string word;
        string result = "";
        int word_index = 1;
        
        // Extract words separated by spaces
        while (ss >> word) {
            // Append a space if this isn't the very first word
            if (word_index > 1) {
                result += " ";
            }
            
            // Rules 1 & 2: Process the start of the word
            if (isVowel(word[0])) {
                result += word + "ma";
            } else {
                // Move the first character to the end and append "ma"
                result += word.substr(1) + word[0] + "ma";
            }
            
            // Rule 3: Append 'a' repeated 'word_index' times
            result += string(word_index, 'a');
            
            word_index++;
        }
        
        return result;
    }
};