class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int five = 0;
        int ten = 0;
        
        for (int bill : bills) {
            if (bill == 5) {
                // No change required, collect the bill
                five++;
            } 
            else if (bill == 10) {
                // Requires $5 in change
                if (five == 0) return false;
                five--;
                ten++;
            } 
            else { // bill == 20
                // Requires $15 in change. 
                // Priority 1 (Greedy): Give a $10 and a $5 to save your flexible $5 bills.
                if (ten > 0 && five > 0) {
                    ten--;
                    five--;
                } 
                // Priority 2: Fall back to three $5 bills if no $10 is available.
                else if (five >= 3) {
                    five -= 3;
                } 
                // Out of valid combinations to provide change.
                else {
                    return false;
                }
            }
        }
        
        return true;
    }
};