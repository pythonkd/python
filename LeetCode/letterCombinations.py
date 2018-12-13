class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        a = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        return p(digits, a)


def p(nums, a):
    if len(nums) == 1:
        return [i for i in a[nums]]
    else:
        return [i + j for i in p(nums[0], a) for j in p(nums[1:], a)]