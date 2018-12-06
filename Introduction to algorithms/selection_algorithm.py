def selection_algorithm(nums):
    for j in range(len(nums)-1): #c1*n
        a = nums[j] # c2*n
        index = j   # c3*n
        minindex = j # c4*n
        for i in nums[j:]: #Σ()
            if a > i:
                a = i
                minindex = index
            index += 1
        nums[minindex], nums[j]= nums[j], a
    return nums
def test():
    a = selection_algorithm([0])
    assert a == [0]
    a = selection_algorithm([2,1,6,3,4,8,5,7])
    assert a == [1,2,3,4,5,6,7,8]
    print('successful')
if __name__ == '__main__':
    test()