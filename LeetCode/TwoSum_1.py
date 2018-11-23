class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = sorted(nums)
        l = 0
        r = len(s) - 1

        while l < r:
            t = s[r] + s[l]
            if t == target:
                al = s[l]
                ar = s[r]
                break
            elif t > target:
                r -= 1
                if l < r and s[r] == s[r + 1]:
                    r -= 1
            else:
                l += 1
                if l < r and s[l] == s[l - 1]:
                    l += 1
        l = nums.index(al)
        nums.reverse()
        r = len(nums) - 1 - nums.index(ar)
        return sorted([l, r])