import random , time
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


class MergeSort(object):
    def __init__(self, nums):
        self.nums = nums
    def __len__(self):
        return len(self.nums)
    def sort(self):
        if len(self) == 0:
            raise Exception('the array is empty!')
        elif len(self) == 1:
            return self.nums
        else:
            x = []
            t = len(self) // 2
            nums_1 = self.nums[:t]
            nums_2 = self.nums[t:]
            nums_1 = InsertionSort(nums_1).sort()
            nums_2 = InsertionSort(nums_2).sort()
            while nums_1 != [] and nums_2 != []:
                a = nums_1[0]
                b = nums_2[0]
                if a <= b:
                    x.append(a)
                    nums_1.remove(a)
                else:
                    x.append(b)
                    nums_2.remove(b)
            if len(nums_1) > len(nums_2):
                x.extend(nums_1)
            else:
                x.extend(nums_2)
            return x
if __name__ == '__main__':
    start = time.time()
    y = [i for i in range(15000)]
    random.shuffle(y)
    s = MergeSort(y).sort()
    end = time.time()
    print(end - start)