class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        // Bước 1: Sắp xếp cả hai mảng theo thứ tự tăng dần
        // g: độ tham lam của trẻ, s: kích thước bánh quy
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        
        int childIndex = 0;  // Con trỏ duyệt danh sách trẻ em
        int cookieIndex = 0; // Con trỏ duyệt danh sách bánh quy
        
        // Bước 2: Duyệt cho đến khi hết trẻ em hoặc hết bánh quy
        while (childIndex < g.size() && cookieIndex < s.size()) {
            // Nếu kích thước bánh quy s[cookieIndex] đủ lớn cho trẻ g[childIndex]
            if (s[cookieIndex] >= g[childIndex]) {
                // Trẻ này đã hài lòng, chuyển sang đứa trẻ tiếp theo
                childIndex++;
            }
            // Dù trẻ có hài lòng hay không, ta vẫn phải chuyển sang chiếc bánh tiếp theo
            // (vì bánh hiện tại quá nhỏ hoặc đã được ăn)
            cookieIndex++;
        }
        
        // Số trẻ hài lòng chính là số lần childIndex được tăng lên
        return childIndex;
    }
};