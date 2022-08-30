# solution in python3

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        finlist = []
        for i in range(l):
            for j in range(i+1,l):
                sum = nums[i] + nums[j]
                if sum == target:
                    finlist.insert(0, i)
                    finlist.insert(1, j)
                    
        return finlist
