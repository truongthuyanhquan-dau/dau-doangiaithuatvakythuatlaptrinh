class Solution {
public:
    string reformatNumber(string number) {
        // Step 1: Extract all digits, filtering out spaces and dashes
        string digits = "";
        for (char c : number) {
            if (isdigit(c)) {
                digits += c;
            }
        }
        
        string result = "";
        int i = 0;
        int n = digits.length();
        
        // Step 2: Group into blocks of 3 as long as more than 4 digits remain
        while (n - i > 4) {
            result += digits.substr(i, 3) + "-";
            i += 3;
        }
        
        // Step 3: Format the remaining 4 or fewer digits
        int remaining = n - i;
        if (remaining == 4) {
            // 4 digits left -> split into two blocks of 2 (XX-XX)
            result += digits.substr(i, 2) + "-" + digits.substr(i + 2, 2);
        } else {
            // 2 or 3 digits left -> take them as a single block
            result += digits.substr(i, remaining);
        }
        
        return result;
    }
};