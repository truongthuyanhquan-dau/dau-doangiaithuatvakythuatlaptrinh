class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> answer;
        // Chúng ta cần trả về mảng 1-indexed (bắt đầu từ 1 đến n)
        for (int i = 1; i <= n; ++i) {
            
            // Trường hợp 1: Chia hết cho cả 3 và 5 (tức là i % 15 == 0)
            if (i % 3 == 0 && i % 5 == 0) {
                answer.push_back("FizzBuzz");
            } 
            // Trường hợp 2: Chỉ chia hết cho 3
            else if (i % 3 == 0) {
                answer.push_back("Fizz");
            } 
            // Trường hợp 3: Chỉ chia hết cho 5
            else if (i % 5 == 0) {
                answer.push_back("Buzz");
            } 
            // Trường hợp 4: Không chia hết cho số nào ở trên
            else {
                // Chuyển số nguyên i thành chuỗi (string)
                answer.push_back(to_string(i));
            }
        }
        return answer;
    }
};
 