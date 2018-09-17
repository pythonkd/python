def is_stressful(subj):
    if subj.isupper() or subj[-3:] == 3*'!':
        return True
    global t
    a = subj.lower()
    t = a.split()
    b = ('help', 'asap', 'urgent')
    for i in b:
        if judge1(i):
            return True
    return False
def judge1(n):
    for i in t:
        if judge2(i,n):
            return True
    return False
def judge2(string,n):
    for i in n:
        if i not in string:
            return False
    return True
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')