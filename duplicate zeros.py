class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        int n = arr.size();
        int zeroes = 0;
        int length = n - 1; 

        // 1. Calculate how many zeroes can actually be duplicated within bounds
        for (int i = 0; i <= length - zeroes; i++) {
            if (arr[i] == 0) {
                // Special edge case: The zero is right at the boundary.
                // It can fit once, but its duplicate would discard the last position.
                if (i == length - zeroes) {
                    arr[n - 1] = 0; 
                    length--; 
                    break;
                }
                zeroes++;
            }
        }

        // 2. Write elements backward from the determined source boundary
        int last_source_idx = length - zeroes;
        int write_idx = n - 1;

        for (int i = last_source_idx; i >= 0; i--) {
            if (arr[i] == 0) {
                arr[write_idx] = 0;
                arr[write_idx - 1] = 0;
                write_idx -= 2;
            } else {
                arr[write_idx] = arr[i];
                write_idx--;
            }
        }
    }
};