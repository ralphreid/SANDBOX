class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]`
        """
        
        sums = []
        
        # check each element in array
        for i in range(0, len(nums)):
            
            # check each otehr element in the array
            for j in range(i+1, len(nums)):
                
                # determine if two element sum to target
                if (nums[i] + nums[j] == target):
                    sums.append(i)
                    sums.append(j)
            
        # retun all pairs of integers that sum to S
        return sums
