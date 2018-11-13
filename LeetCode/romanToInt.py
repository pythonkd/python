class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = {'I': 1, "IV": 4, 'V': 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500,
             "CM": 900, "M": 1000}
        n = 0
        while s:
            i = 2
            if s[:i] not in L:
                i -= 1
            n += L[s[:i]]
            s = s[i:]
        return n
