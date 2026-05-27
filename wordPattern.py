class Solution {
public:
    bool wordPattern(string pattern, string s) {
        
        vector<string> words;
        stringstream ss(s);
        string word;
        
        // Bước 1: Tách các từ trong s và lưu vào vector
        while (ss >> word) {
            words.push_back(word);
        }

        // Bước 2: Kiểm tra số lượng phần tử
        if (pattern.length() != words.size()) {
            return false;
        }

        // Bước 3: Sử dụng 2 map để đảm bảo quan hệ song ánh (bijection)
        unordered_map<char, string> charToWord;
        unordered_map<string, char> wordToChar;

        for (int i = 0; i < pattern.length(); ++i) {
            char c = pattern[i];
            string w = words[i];

            // Kiểm tra ánh xạ từ ký tự sang từ
            if (charToWord.count(c) && charToWord[c] != w) {
                return false;
            }
            
            // Kiểm tra ánh xạ từ từ sang ký tự
            if (wordToChar.count(w) && wordToChar[w] != c) {
                return false;
            }

            // Thiết lập ánh xạ nếu chưa tồn tại
            charToWord[c] = w;
            wordToChar[w] = c;
        }

        return true;
    }
};