class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = {}
        for i, num in enumerate(nums): #enumerate gives you both index, value
            if num in needed: 
                return[needed[num], i] #the value of needed and its index
            else:
                needed[target - num] = i #else needed[complement] = index
                #if num is not in needed, complement = key and index = value
