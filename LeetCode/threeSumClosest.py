class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        A = nums[0] + nums[1] + nums[2]
        gap = abs(A - target)
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k] - target
                if s == 0:
                    return target
                if gap > abs(s):
                    gap = abs(s)
                    A = s + target
                if s < 0:
                    j += 1
                    if j < k and nums[j] == nums[j-1]:
                        j += 1
                elif s > 0:
                    k -= 1
                    if j < k and nums[k] == nums[k+1]:
                        k -= 1
        return A

if __name__ == '__main__':
    a = Solution()
    print(a.threeSumClosest([1, -3, 3, 5, 4, 1], 1))