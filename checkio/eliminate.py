#Your optional code here
#You can import some modules or create additional functions

from collections import Counter
def checkio(data: list) -> list:
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.
    x=sorted(Counter(data).most_common(),key=lambda x:x[1])
    global S
    S=[]
    for i in list(filter(compare,x)):
        S.append(i[0])
    l=list(filter(isin,data))
    return l
def isin(n):
    if n in S:
        return True
    else:
        return False
def compare(n):
    if n[1]==1:
        return False
    return True

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")