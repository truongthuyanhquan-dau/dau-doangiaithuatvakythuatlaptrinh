class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int total_drunk = 0;
        int empty_bottles = 0;
        
        while (numBottles > 0) {
            // 1. Drink all available full bottles
            total_drunk += numBottles;
            empty_bottles += numBottles;
            
            // 2. Calculate how many full bottles we get from trading
            numBottles = empty_bottles / numExchange;
            
            // 3. Keep track of any leftover empty bottles that couldn't be traded yet
            empty_bottles = empty_bottles % numExchange;
        }
        
        return total_drunk;
    }
};