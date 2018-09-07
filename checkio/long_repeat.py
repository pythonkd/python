def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    n=''
    a=''
    for i in line:
        if i!=n:
            n=i
            a=a+','+i
        else :
            a=a+i
    b=a.strip(',').split(',')
    sum=0
    for i in b:
        if sum<len(i):
            sum=len(i)
    # your code here
    return sum
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')