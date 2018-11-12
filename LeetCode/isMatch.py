import re
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        t = re.compile(p)
        u = re.search(t, s)
        if u:
            u = u.span()
            l = u[0]
            r = u[1]
            if s[l:r] == s:
                return True
        return False