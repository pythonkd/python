import random, time
class InsertionSort(object):
    def __init__(self, nums):
        self.nums = nums
    def __len__(self):
        return len(self.nums)
    def sort(self):
        if len(self) == 0:
            raise Exception('the array is empty!')
        j = 1
        a = [self.nums[0]]
        while j < len(self):
            n = self.nums[j]
            t = 0
            while t < len(a):
                if a[t]< n:
                    t += 1
                else:
                    break
            a.insert(t, n)
            j += 1
        return a

if __name__ == '__main__':
    start = time.time()
    x = [i for i in range(15000)]
    random.shuffle(x)
    s = InsertionSort(x).sort()
    end = time.time()
    print(end - start)