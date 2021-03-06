class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        j = 1
        
        while i+j < len(nums):
            if nums[i] != 0:
                i += 1
            elif nums[i+j] == 0:
                j += 1
            else:
                nums[i], nums[i+j] = nums[i+j], nums[i]
                
        return nums
                    
                
 """
 i: points the position of non-zeros
 j: points the position of zeros
 """
j = 0

for i in range(len(nums)):
    al = nums[i]
    if al != 0:
        nums[i], nums[j] = nums[j], nums[i]
        j += 1
