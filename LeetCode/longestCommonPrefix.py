class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        s = strs[0]
        for i in strs[1:]:
            while s != i[:len(s)]:
                s = s[:-1]
        return s
