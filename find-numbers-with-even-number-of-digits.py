lass Solution {
public:
    int findNumbers(vector<int>& nums) {
        int even_digit_count = 0;
        
        for (int num : nums) {
            // Using direct range bounds based on constraints (1 <= nums[i] <= 10^5).
            // A number has an even number of digits if it has 2 digits, 4 digits, or 6 digits.
            if ((num >= 10 && num <= 99) || 
                (num >= 1000 && num <= 9999) || 
                (num == 100000)) {
                even_digit_count++;
            }
        }
        
        return even_digit_count;
    }
};