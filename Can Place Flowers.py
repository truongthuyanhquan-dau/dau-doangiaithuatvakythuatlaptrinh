class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        
        count = 0
        size = len(flowerbed)
        
        for i in range(size):
            
            if count >= n:
                return True
            
            if flowerbed[i] == 0:
                
                prev_is_empty = (i == 0) or (flowerbed[i - 1] == 0)
                
               
                next_is_empty = (i == size - 1) or (flowerbed[i + 1] == 0)
                
                if prev_is_empty and next_is_empty:
                    flowerbed[i] = 1 
                    count += 1
                    
        return count >= n