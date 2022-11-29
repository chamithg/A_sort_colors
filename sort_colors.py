class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        i = 0
        
        def swap(x,y):
            tmp = nums[x]
            nums [x] = nums [y]
            nums [y] = tmp
        
        while i <= right:
            if nums[i]== 0:
                swap(i,left)
                left +=1
            elif nums[i]== 2:
                swap(i,right)
                right -= 1
                i -=1
            
            i+=1
            
        
        
        return nums
        
obj = Solution()
nums = [1,2,0]
print(obj.sortColors(nums)) 
