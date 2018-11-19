import bisect
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        t = bisect.bisect_right(nums, 0)
        for i in range(t):
            if i == 0 or nums[i] >nums[i-1]:
                l = i+1
                r = len(nums) -1
                while l < r:
                    A = nums[i] + nums[l] + nums[r]
                    if A == 0:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while r > l and nums[r+1] == nums[r]:
                            r -= 1
                    elif A >0:
                        r -= 1
                    elif A < 0:
                        l += 1
        return res