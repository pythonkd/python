# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l < r:
            mid = (l+r)//2
            # print(isBadVersion(mid))
            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid
        return l