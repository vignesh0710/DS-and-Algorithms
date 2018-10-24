class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target in nums and 0 in nums:
            return nums.index(target),nums.index(0)
        else:
            for each_num in nums:
                if each_num in nums and (target-each_num) in nums and nums.index(each_num) != nums.index(target-each_num):     
                    return nums.index(each_num),nums.index(target-each_num)
                
                
s1 = Solution()
nums = [1,3,2,11,4]
target = 5
print (s1.twoSum(nums,target))
        
