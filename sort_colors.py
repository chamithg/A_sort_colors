class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        runner = 0
        
        while runner< len(nums):
            if nums[runner] == 0:
                nums.pop(runner)
                nums.insert(0,0)
                runner +=1
            elif nums[runner] == 2:
                nums.append(2)
                nums.pop(runner)
                # runner +=1
            else:
                runner +=1
        
        
        return nums
        
obj = Solution()
nums = [1,2,0]
print(obj.sortColors(nums)) 
