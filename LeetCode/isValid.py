class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 关键要知道它最近一次匹配的是谁 所以用到栈
        stack = []
        dick = {')':"(", '}':'{', ']':'['}
        for i in s:
            if i not in dick:
                stack.append(i)
            else:
                if stack and dick[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack