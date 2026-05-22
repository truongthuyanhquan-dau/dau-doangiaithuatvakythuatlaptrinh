

class Solution {
public:
    vector<int> distributeCandies(int candies, int num_people) {
        vector<int> distribution(num_people, 0);
        int current_gift = 1;
        int person_index = 0;
        
        while (candies > 0) {
            // Give out the planned amount, or whatever leftover candies remain
            int give = min(current_gift, candies);
            
            distribution[person_index] += give;
            candies -= give;
            
            // Advance parameters for the next iteration
            current_gift++;
            person_index = (person_index + 1) % num_people; // Clean loop wrap-around
        }
        
        return distribution;
    }
};