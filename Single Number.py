class Solution(object):
    def singleNumber(self, nums):
        mask = 0
        for i in range(len(nums)):
            mask = mask ^ nums[i]
        pos = 0
        new_mask = mask
        while (new_mask & 1 != 1):
            pos += 1
            new_mask >>= 1
        new_mask = 1 << pos
        temp = 0
        for i in range(len(nums)):
            if (nums[i] & new_mask):
                temp = temp ^ nums[i]
        list1 = [temp, mask ^ temp]
        return list1
        
print (Solution().singleNumber([11,22,33,44,55,33,11,22]))
