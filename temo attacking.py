class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int n = timeSeries.size();
        if (n == 0) return 0;

        int totalSeconds = 0;

        // Iterate through all attacks except the last one
        for (int i = 0; i < n - 1; ++i) {
            // Calculate the time elapsed between this attack and the next
            int gap = timeSeries[i + 1] - timeSeries[i];
            
            // If the gap is smaller than duration, we only add the gap.
            // Otherwise, we add the full duration.
            totalSeconds += min(gap, duration);
        }

        // The final attack always lasts for the full duration
        totalSeconds += duration;

        return totalSeconds;
        
    }
};