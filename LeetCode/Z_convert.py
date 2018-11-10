class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        t = [[] for i in range(numRows)]
        j = 0
        st = 0
        for i in s:
            t[j].append(i)
            if st == 0:
                j+=1
            else:
                j -= 1
            if j in (numRows-1,0):
                if st == 0:
                    st =1
                else:
                    st =0
        s = ''
        for i in t:
            for j in i:
                s += j
        return s