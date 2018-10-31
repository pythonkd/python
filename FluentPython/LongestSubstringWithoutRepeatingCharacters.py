class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        u = []
        t = len(s)
        # 这是一个移动窗口，先固定i再对j相加
        for i in range(t):
            j = i
            while s[j] not in s[i:j] :
                j += 1
                if t == j:
                    break
            u.append(s[i:j])
        t = sorted(u, key=lambda x:len(x), reverse=True)[0]
        return len(t)