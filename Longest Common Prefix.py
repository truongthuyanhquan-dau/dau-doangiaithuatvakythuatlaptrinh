class Solution(object):
    def longestCommonPrefix(self, strs):
        
        if not strs:
            return ""
        
        first_word = strs[0]
        
        for i in range(len(first_word)):
            char = first_word[i]
            
            for j in range(1, len(strs)):
            
                if i == len(strs[j]) or strs[j][i] != char:
                    
                    return first_word[:i]
        
        return first_word