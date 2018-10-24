class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target in nums and 0 in nums:
            print ("in if case")
            return nums.index(target),nums.index(0)
        else:
            print ("in else case")
            for each_num in nums:
                if each_num in nums and (target-each_num) in nums and nums.index(each_num) != nums.index(target-each_num):
                    
                    return nums.index(each_num),nums.index(target-each_num)
                    
        