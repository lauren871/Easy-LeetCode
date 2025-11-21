class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_map = {} #stores number as key and it's index as value

        for i, num in enumerate(nums): #Loop through the list with index and value
            complement = target - num #Find the complement needed to complete pair
            if complement in num_map: #Check if complement is in hashmap already
                return [num_map[complement], i] #Return complement index and current index
            num_map[num] = i #If not, store current number and index in hashmap
