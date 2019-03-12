from collections import deque
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s = deque()
        d = {}
        for i in nums2:
            while s and s[-1] < i:
                d[s.pop()] = i
            s.append(i)
        return [d[i] if i in d else -1 for i in nums1]