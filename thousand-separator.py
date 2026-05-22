class Solution {
public:
    string thousandSeparator(int n) {
        // Handle the base case explicitly
        if (n == 0) {
            return "0";
        }
        
        string result = "";
        int digit_count = 0;
        
        // Process the number from right to left
        while (n > 0) {
            // Insert a dot separator every 3 digits, provided there are more digits ahead
            if (digit_count > 0 && digit_count % 3 == 0) {
                result += ".";
            }
            
            // Append the last digit as a character
            result += to_string(n % 10);
            digit_count++;
            
            // Shave off the last digit
            n /= 10;
        }
        
        // Flip the string back to its proper order
        reverse(result.begin(), result.end());
        
        return result;
    }
};