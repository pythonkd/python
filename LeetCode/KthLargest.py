import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.min_heap = []
        self.capacity = k
        self.iterable = nums
        self.get()

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.min_heap) >= self.capacity:
            if val > self.min_heap[0]:
                heapq.heapreplace(self.min_heap, val)
        else:
            heapq.heappush(self.min_heap, val)

        return self.min_heap[0]

    def get(self):
        for item in self.iterable:
            self.add(item)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)