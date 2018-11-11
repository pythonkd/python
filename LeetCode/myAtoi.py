class Solution:
    def myAtoi(self, str):
        num = ["{}".format(i) for i in range(10)]
        nums = num + ['-', '+']
        l = len(str)
        for i in range(len(str)):
            if str[i] == ' ':
                continue
            elif str[i] in nums:
                l = i
                break
            else:
                return 0
        r = len(str)
        for i in range(l + 1, len(str)):

            if str[i] in num:
                #                 print(str[i])
                continue
            else:
                #                 print(i)
                r = i
                break
        #         print(str[l:r])
        if str[l:r] in ['', '-', '+']:
            return 0
        n = int(str[l:r])
        L = pow(-2, 31)
        R = pow(2, 31) - 1
        if n < L:
            return L
        if n > R:
            return R
        return n