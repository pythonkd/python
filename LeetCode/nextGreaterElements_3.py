from collections import deque
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        d = deque()
        a = [None]*len(nums)
        max_val = max(nums)
        for i, j in enumerate(nums):
            while d and d[-1][1] < j:
                t = d.pop()
                a[t[0]] = j
            if j != max_val:
                d.append([i, j])
            else:
                a[i] = -1
        # print(d)
        for i in nums:
            if len(d) == 0:
                break
            while d and d[-1][1] < i:
                t = d.pop()
                a[t[0]] = i
        return a