class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        t = abs(x)
        a = int(str(t)[::-1])
        if x < 0:
            a = -a
        L = pow(-2,31)
        R = pow(2,31)-1
        if (a > R) or(a < L):
            return 0
        return a