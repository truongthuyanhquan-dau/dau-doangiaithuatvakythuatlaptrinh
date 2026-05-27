class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        // map để lưu trữ: [tổng của nums1[i] + nums2[j]] -> [số lần xuất hiện của tổng đó]
        unordered_map<int, int> sumCount;
        int count = 0;

        // Bước 1: Duyệt qua nums1 và nums2 để tính tất cả các tổng có thể có
        for (int i : nums1) {
            for (int j : nums2) {
                sumCount[i + j]++;
            }
        }

        // Bước 2: Duyệt qua nums3 và nums4
        // Tìm xem có tổng nào là -(k + l) đã tồn tại trong map không
        for (int k : nums3) {
            for (int l : nums4) {
                int target = -(k + l);
                if (sumCount.find(target) != sumCount.end()) {
                    count += sumCount[target];
                }
            }
        }

        return count;
    }
};