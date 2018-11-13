class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        s = 0
        x2 = len(height)-1
        x1 = 0
        while x1 < x2:
            y1 = height[x1]
            y2 = height[x2]
            s = max(s, (x2-x1)*min(y1,y2))
            if y1 > y2:
                x2 -= 1
            else:
                x1 += 1
        return s