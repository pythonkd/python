class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # return self.merge_sort(nums)[-k]
        nums.sort()
        return nums[-k]

    # def fast_sort(self, nums):
    #     if len(nums)<2:
    #         return nums
    #     else:
    #         pivote = nums[0]
    #         l = [i for i in nums[1:] if i <=pivote]
    #         r = [i for i in nums[1:] if i > pivote]
    #         return self.fast_sort(l) + [pivote] + self.fast_sort(r)

#     def merge_sort(self, nums):
#         if len(nums) < 2:
#             return nums
#         else:
#             mid = len(nums) // 2
#             return self.sort_nums(self.merge_sort(nums[:mid]), self.merge_sort(nums[mid:]))

#     def sort_nums(self, left, right):
#         i, j = 0, 0
#         s = []
#         l_len, r_len = len(left), len(right)
#         while i < l_len and j < r_len:
#             if left[i] < right[j]:
#                 s.append(left[i])
#                 i += 1
#             else:
#                 s.append(right[j])
#                 j += 1
#         if i < l_len:
#             s += left[i:]
#         else:
#             s += right[j:]
#         return s