class Solution (object):
    def containsDuplicate(self,nums):
        ktra = set()
        for n in nums:
            if n in ktra:
                return True
            ktra.add(n)
        return False
